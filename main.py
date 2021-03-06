#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Script python para reiniciar un minador dependiendo del minimun_hash  (default = 05.00)
	
	Instruciones para Instalar:
		1. Poner el archivo en el minador bajo la ruta: /home/ethos
		2. Iniciar una tarea programada o crontab	
			2.1  Terminal: crontab -e
			2.2  añadir las siguientes lineas, cambiar a conveniencia
					# monitor python
					@reboot ( sleep 300 ;/usr/bin/python /home/ethos/carpeta_nombre/main.py)
					*/10 * * * * /usr/bin/python /home/ethos/carpeta_nombre/main.py
			2.3 Guardar + Salir 
		
		3. Disfrutar :)			

"""
import os
import re
import subprocess
from subprocess import Popen, PIPE

from dev.handling import Handling
from dev.email import sendEmailAlert

__author__ = "Eduardo Xavier Castro Morales"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Eduardo Morales"
__email__ = "cuentasdevelopers@gmail.com"
__status__ = "Prototype"



def main():
	minimun_hash = format(float(5), '.2f')
	hostname = ''
	rack_loc = ''
	# Haciendo Ping a google dns (solo unix)
	with open(os.devnull, 'w') as DEVNULL:
	    try:
	        subprocess.check_call(
	            ['ping', '-c', '1', '8.8.8.8'],
	            stdout=DEVNULL,  
	            stderr=DEVNULL
	        )
	        is_online = True
	    except subprocess.CalledProcessError:
	        is_online = False

	if is_online == True:
	    # tomamos del update_data el rack_loc o hostname  (con la finalidad de enviarselo a un servicio que nos avise)
	    update_data = subprocess.check_output(['/opt/ethos/bin/update'])
	    for data in update_data.splitlines():
	    	if 'rack_loc:   ' in data:
	    		rack_loc_list = re.findall(r'\w+', data)
	    		if len(rack_loc_list) > 1:
	    			rack_loc = rack_loc_list[1]
	    	elif 'hostname:   ' in data:
	    		host_list = re.findall(r'\w+', data)
	    		if len(host_list) > 1:
	    			hostname = host_list[1]
	    	else:
	    		pass

	    # tomamos los hashes de cada GPU
	    file_hashes = '/var/run/ethos/miner_hashes.file'
	    p = Popen(['tail','-1',file_hashes], stderr=PIPE, stdout=PIPE)
	    res,err = p.communicate()

	    if err:
	    	print(err.decode())
	    else:
	    	gpu_hashes = res.split(" ")
	    	is_need_reboot = False
	    	for gpu_hash in (gpu_hashes):
	    			if float(gpu_hash) < float(minimun_hash):
	    				is_need_reboot = True

	    	if is_need_reboot:
	    		handling = Handling()
	    		counter = handling.readTheCounterFile()
	    		if int(counter) < 4:
	    			handling.addToTheCounterFile(counter)
	    			os.system("/opt/ethos/bin/r")
	    		elif int(counter) == 5:
	    			handling.addToTheCounterFile(counter)
	    			sendEmailAlert(str(rack_loc))
	    		else:
	    			pass				
	else:
		print(" No Tenemos Internet :( ")
		exit()

if __name__ == '__main__':
	main()
	#handling = Handling()
	#counter = handling.readTheCounterFile()
	#handling.addToTheCounterFile(counter)
	#handling.resetCounterFile()
	#sendEmailAlert('sm120')
# EthosMonitorGpu

Script python para reiniciar un minador dependiendo del minimun_hash  (default = 05.00)

### Prerequisites

Python > 2.7

### Installing

Instruciones para Instalar:

```
1. Poner el archivo en el minador bajo la ruta: /home/ethos

2. Iniciar una tarea programada o crontab	
			2.1  Terminal: crontab -e
			2.2  añadir las siguientes lineas, cambiar a conveniencia
					# monitor python
					@reboot ( sleep 300 ;/usr/bin/python /home/ethos/carpeta_nombre/main.py)
					
					*/10 * * * * /usr/bin/python /home/ethos/carpeta_nombre/main.py
			2.3 Guardar + Salir 
		
3. Disfrutar :)			
```

## Built With

* [Python](https://www.python.org)

## Versioning

* **Prototype** 

## Author

* **Eduardo Morales** - *Initial work* - 



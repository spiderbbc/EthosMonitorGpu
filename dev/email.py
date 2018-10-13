import smtplib



def sendEmailAlert(rack_loc):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	#Next, log in to the server
	server.login("monitorethos@gmail.com", "ethoslive")

	#Send the mail
	msg = "Hola! el minador %s ya a alcanzado el tope maximo de reinicios se solicita su intervencion, por favor setear el contador" % rack_loc # The /n separates the message from the headers
	server.sendmail("monitorethos@gmail.com", "cuentasdevelopers@gmail.com", msg)
	print('Email enviado ..')
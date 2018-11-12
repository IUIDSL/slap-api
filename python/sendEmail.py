#!/usr/bin/python

import smtplib, sys
from email.MIMEText import MIMEText


def sendEmail(receivers, title, body, sender = 'chembiospaces@gmail.com', usr = 'chembiospaces', password = 'chem2bio2rdf', servername = "smtp.gmail.com", cc = True):
	#send a copy to sender
	if cc:
		receivers.append(sender)

	msg = MIMEText(body)
	msg['From'] = sender
	msg['To'] = ', '.join(receivers)
	msg['Subject'] = title

	try:
		server = smtplib.SMTP(servername,587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(usr, password)
		server.sendmail(sender,receivers,msg.as_string())
		server.quit
	except SMTPException:
   		print "Error: unable to send email"



if __name__ == '__main__':
	receivers = ['smallerbear@gmail.com', 'chembiospace@gmail.com']
	title = "Email Test"
	body = """
	blank
	"""
	sendEmail(receivers, title, body, sender='chembiospaces@gmail.com', usr = 'chembiospaces', password = 'chem2bio2rdf', cc = True)


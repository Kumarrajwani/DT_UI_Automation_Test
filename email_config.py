import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email():
	fromaddr = "mahesh.kumar@distribusion.com"
	toaddr = "mahesh.kumar@distribusion.com"
 
	msg = MIMEMultipart()
 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Test Case Result of the Contact Page (Distribusion.com)"
	body = "Please check the attachment for the test case result"
 
	msg.attach(MIMEText(body, 'plain'))
 
	filename = "Test_Results.txt"
	attachment = open(filename)
 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	
	msg.attach(part)
 
	server = smtplib.SMTP('alt1.aspmx.l.google.com')
	
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	print("Mail Sent")
	
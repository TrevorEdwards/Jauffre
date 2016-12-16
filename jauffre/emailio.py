import poplib
import socket
import smtplib
import config_manager as cm
import sendgrid
import base64

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=cm.get('Keys','sendgrid'))

def get():
    pass

def send_mail(send_from, send_to, subject, text, files=[]):
	from_email = Email(send_from)
	to_email = Email(send_to)	
	content = Content('text/plain', text)
	mail = Mail(from_email, subject, to_email, content)
	for i in range(len(files)):
		wow = Attachment()
		wow.set_filename('wow' + str(i))
		wow.set_content(base64.b64encode(open(files[i], 'rb').read()))
		wow.set_type("image/jpg")
		wow.set_disposition("attachment")
		mail.add_attachment(wow)	
	sg.client.mail.send.post(request_body=mail.get())


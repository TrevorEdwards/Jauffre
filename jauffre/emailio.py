import poplib
import socket
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
#from email import parser

def get():
    pass

def send_mail(send_from, send_to, subject, text, files=None):
    pass

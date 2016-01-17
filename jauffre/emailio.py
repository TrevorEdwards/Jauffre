import poplib
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
#from email import parser

def get():
    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user('jauffrebot')
    pop_conn.pass_('jauffredragon')
    #Get messages from server:
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    # Concat message pieces:
    messages = ["\n".join(mssg[1]) for mssg in messages]
    #Parse message into an email object:
    #messages = [parser.Parser().parsestr(mssg) for mssg in messages]
    #for message in messages:
    #    print message
    pop_conn.quit()
    if len(messages) > 0:
        return messages[0]



def send_mail(send_from, send_to, subject, text, files=None):

    msg = MIMEMultipart(
        From=send_from,
        To=COMMASPACE.join(send_to) if type(send_to)==list else send_to,
        Date=formatdate(localtime=True),
        Subject=subject
    )
    
    msg += '\n'
    
    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            msg.attach(MIMEApplication(
                fil.read(),
                Content_Disposition='attachment; filename="%s"' % basename(f),
                Name=basename(f)
            ))


    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    username = ('jauffrebot')
    pwd = ('jauffredragon')
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(username, pwd)
    smtp_server.ehlo()

    smtp_server.sendmail(send_from, send_to, msg.as_string())
    smtp_server.close()

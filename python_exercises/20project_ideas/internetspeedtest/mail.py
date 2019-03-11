"""
Python Program to send email(Works in Python2 and Python3 Versions)
"""
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
  


print("Sending email........................")
gmail_user = '<--Your Gmail Username-->'
gmail_pwd = '<--Your Gmail Password-->'
to=['<--Receivers mailid list-->']
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)

for i in to:
    msg = MIMEMultipart()
    msg['To'] = i
    msg['Subject'] = "<--Your mail Subject-->"
    body = "<--Your mail message-->"
    msg.attach(MIMEText(body, 'plain'))
    filename = "<--Your attachment-->"
    attachment = open("<--File path-->", "<--File Mode-->")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    text = msg.as_string()
    smtpserver.sendmail(gmail_user, to, text)

print('Mail sent Sucessfully')
smtpserver.close()


#************INTERNET SPEED TEST PROGRAM*********************
# __AUTHOR__: VINEEL KUMAR
# VERSION:1.0
#************************************************************

#This program works in Pyhton2 Perfectly
import os
import time
import smtplib
import urllib2
import cookielib
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
  
print ("Current date & time " + time.strftime("%c"))
s=os.system("speedtest-cli --simple")

if s==0:
    #Email Sending code
    print("Sending email........................")
    gmail_user = 'your gmail username'
    gmail_pwd = 'your gmail password'
    to=["---Receivers mail id list----"]
    
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    #header = 'To:' + str(to) + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:From SSSIHL internet speed test program\n'
    for i in to:
        msg = MIMEMultipart()
        msg['To'] = i
        msg['Subject'] = "Your Subject"
        body = "\n Your Message \n\n"
        msg.attach(MIMEText(body, 'plain'))
        filename = "speedtest.log"
        attachment = open("Path of log file", "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        text = msg.as_string()
        smtpserver.sendmail(gmail_user, to, text)
    print('Mail sent Sucessfully')
    smtpserver.close()

    #SMS sending code
    print("Sending SMS...........................")
    username = "Way2sms ID"
    passwd = "Way2sms Password"
    message = "\n Your Message \n\n"
    n=['Receivers mobile number list']
    for i in n:
        number =i 
        message = "+".join(message.split(' '))
        url = 'http://site24.way2sms.com/Login1.action?'
        data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
 
        try:
            usock = opener.open(url, data)
        except IOError:
            print ("Error while logging in.")
            sys.exit(1)
    
        jession_id = unicode(cj).split(u'~')[1].split(u' ')[0]
        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
        opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]

        try:
            sms_sent_page = opener.open(send_sms_url,send_sms_data)
        except IOError:
            print ("Error while sending message" )
            sys.exit(1)

    print ("SMS has been sent.")


else:

    print("Internet was Down")



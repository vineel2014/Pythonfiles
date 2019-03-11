import smtplib
from tkinter import *
import tkinter.messagebox as mbox
def sent():

 to =e1.get()
 gmail_user = 'Enter your gmail username'
 gmail_pwd = 'Enter your gmail password'
 smtpserver = smtplib.SMTP("smtp.gmail.com",587)
 smtpserver.ehlo()
 smtpserver.starttls()
 smtpserver.ehlo
 smtpserver.login(gmail_user, gmail_pwd)
 header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:from vineel python program\n'
 mbox.showinfo('INFORMATION',header)
 msg = header + '\n This is python mail sending program from python \n\n'
 smtpserver.sendmail(gmail_user, to, msg)
 mbox.showinfo('Yes','Mail sent Sucessfully')
 smtpserver.close()

def quit():
 master.destroy()


master = Tk()
Label(master, bg="lime",text="Email id").grid(row=0)

e1 = Entry(master)


e1.grid(row=0, column=1)

master["bg"] = "green"
Button(master, text='send',bg="lime", command=sent).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Quit',bg="lime", command=quit).grid(row=3, column=3, sticky=W, pady=4)

mainloop()


from tkinter import *
import sqlite3 as lite
import sys
import tkinter.messagebox as mbox 


   
con = lite.connect('user.db')
with con:   
 cur = con.cursor()
 cur.execute('''CREATE TABLE IF NOT EXISTS
                      login (username TEXT primary key, password TEXT)''')

def show_entry_fields():
     e=e1.get()
     f=e2.get()

     cur.execute("INSERT INTO login VALUES (?, ?)", (e, f))
   
         
     mbox.showinfo('Yes','User Acccount Created Sucessfully')
  

def login():
         login = e1.get()
         passw = e2.get()
         print (login)
         print(passw)
         con = lite.connect('user.db')
         with con:
          cur = con.cursor()

          cur.execute('select * from login where username=? and password=?',login,passw)
          cur.fetchone() 
    
        # if(cur  not none):
        #exist = cursor.fetchone()
         if cur.rowcount>0:
          print ("\nLogin successful!\n")
         else:
          print ("\nUser doesn't exist or wrong password!\n")

     
def quit():
  master.destroy()


master = Tk()
Label(master, text="Username").grid(row=0)
Label(master, text="Password").grid(row=1)

e1 = Entry(master)
e2 = Entry(master,show="*")


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Register', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Login', command=login).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Quit', command=quit).grid(row=3, column=2, sticky=W, pady=4)


mainloop( )

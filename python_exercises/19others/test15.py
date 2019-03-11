from tkinter import *
import sqlite3 as lite
import sys
import tkinter.messagebox as mbox 


   
con = lite.connect('user.db')
with con:   
 cur = con.cursor()
 cur.execute('''CREATE TABLE IF NOT EXISTS
                      login (username TEXT unique, password TEXT)''')

def show_entry_fields():
     e=e1.get()
     f=e2.get()
     #print(e)
     #print(f)
             
     if(e=='' and f==''):
      mbox.showerror('ERROR','Feilds should not be empty')
     else:
      cur.execute("select * from login where username=? or password=?",(e,f))
      if(cur.fetchone()):
        mbox.showinfo('Yes','User Acccount Already Exists')
      else:
        cur.execute("INSERT INTO login VALUES (?, ?)", (e, f))
        mbox.showinfo('Yes','User Acccount Created Sucessfully')
     
      #print(cur.fetchall())
     #cur.execute("delete from login");
     con.commit()

def login():
         login = e1.get()
         passw = e2.get()
         #print(login)
         #print(passw)
         if login=='' and passw=='':
          mbox.showerror('ERROR','Feilds should not be empty')    
         else:     
          con = lite.connect('user.db')
          with con:
           cur = con.cursor()

           cur.execute('select * from login where username=? and password=?',(login,passw))
    
           if (cur.fetchone()) :
            mbox.showinfo('Yes','You are Successfully Logged in')
           else:
            mbox.showinfo('Error','User doesnot exist or wrong password!\n')
          
def forgot():
         con = lite.connect('user.db')
         with con:
          cur = con.cursor()
         #tkMessageBox.showerror("Tkinter Entry Widget", "Enter a text value")
          g=e1.get()
          h=e2.get()
          if(g=='' and h==''):
           mbox.showerror('ERROR','Feilds should not be empty')
          else:
           cur.execute('update login set password=? where username=?',(h,g))
           mbox.showinfo('Yes','You are Successfully updated your password')
     
def quit():
  master.destroy()


master = Tk()
Label(master, bg="lime",text="Username").grid(row=0)
Label(master,bg="lime", text="Password").grid(row=1)

e1 = Entry(master)
e2 = Entry(master,show="*")


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
master["bg"] = "green"
Button(master, text='Register',bg="lime", command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Login',bg="lime", command=login).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Forgot Password',bg="lime", command=forgot).grid(row=3, column=2, sticky=W, pady=4)
Button(master, text='Quit',bg="lime", command=quit).grid(row=3, column=3, sticky=W, pady=4)


mainloop()



from tkinter import *

root = Tk()
root.title("Note Taker")

def Button1():
	listbox.insert(END, "button1 pressed")

def Button2():
	listbox.insert(END, "button2 pressed")

def Button3():
	listbox.insert(END, "button3 pressed")
	
button1 = Button(root, text="button1", command = Button1)
button2 = Button(root, text="button2", command = Button2)
button3 = Button(root, text="button3", command = Button3)

text = Entry(root)

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

text.pack()
button1.pack()
button2.pack()
button3.pack()
listbox.pack()
scrollbar.pack()

root.mainloop()

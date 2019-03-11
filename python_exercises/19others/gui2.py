from tkinter import *
root = Tk()
svalue = StringVar() # defines the widget state as string
w = Entry(root,textvariable=svalue) # adds a textarea widget
w.pack()
def act():
    print ("you entered")
    print ('%s' % svalue.get())
foo = Button(root,text="Press Me", command=act)
foo.pack()
root.mainloop()

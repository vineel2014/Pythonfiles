# Log in
def LogIn():
    name=input("Please enter your name: ")
    file = open(name.lower() + " profile.txt", "r")
#+=========GUI===========GUI============GUI===========+

    #mport modules
    import tkinter
    import time

    #---Window---#
    #make window
    window = tkinter.Tk()
    #change title
    window.title("Python Games Login")
    #change size
    window.geometry("270x210")
    #change window icon
    window.wm_iconbitmap("Login icon.ico")
    #change window colour
    window.configure(bg="#39d972")

    #---Commands---#
    #go
    def callback():
        line = file.readlines()
        username = user.get()
        password = passw.get()
        if username == line[1] and password == line[2]:
            message.configure(text = "Logged in.")
        else:
            message.configure(text = "Username and password don't match the account \n under the name;\n \'" + name + "\'. \nPlease try again.")
    #---Widgets---#
    #labels
    title1 = tkinter.Label(window, text="--Log in to play the Python Games--\n", bg="#39d972")
    usertitle = tkinter.Label(window, text="---Username---", bg="#39d972")
    passtitle = tkinter.Label(window, text="---Password---", bg="#39d972")
    message = tkinter.Label(window, bg="#39d972")

    #text entry windows
    user = tkinter.Entry(window)
    passw = tkinter.Entry(window, show='*')

    #buttons
    go = tkinter.Button(window, text="Log in!", command = callback, bg="#93ff00")

    #pack widgets
    title1.pack()
    usertitle.pack()
    user.pack()
    passtitle.pack()
    passw.pack()
    go.pack()
    message.pack()

    #start window
    window.mainloop()

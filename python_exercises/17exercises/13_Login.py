import time,string

db = {}
usrnmsg = 'Enter user name: '
paswdmsg = 'Enter user password: '
timestamp = []
valname = string.ascii_letters + string.digits + '_'

def NewAc():
    while True:
        user = input(usrnmsg).strip().lower()
        for i in user:
            if i not in valname:
                print ('Username is Invalid')
                return
            
        if user in db:
            print ('\nUsername already exists. try Again\n')
        else:
            break
    passwd = input(paswdmsg).strip()
    db[user] = passwd
    print ('\nUser Account Created\n')

def OldAc():
    count = 0
    user = input(usrnmsg).strip().lower()
    for i in user:
        if i not in valname:
            print ('Username is Invalid')
            return
    while True and count <3:
        passwd = input(paswdmsg).strip()
        password = db.get(user)
        
        if password != passwd and password != None :
            print ('\nInvalid Password.Try Again\n')
            count += 1

        elif password == None:
            msg = ("""\nUser Id doesn't exist. Do you want to create one?
    (Y)es
    (N)o

    Enter your choice: """)

            while True:
                x = input(msg).strip().lower()
                if x[0] not in 'yn':
                    print ('\nInvalid.choose again\n')
                else:
                    break
                
            if x[0] == 'y':
                pwd = input(paswdmsg).strip()
                db.setdefault(user,pwd)
                print ('\nAccount Created\n')
                
                break
            
            elif x[0] == 'n':
                break
                
        elif password == passwd:
            tm = time.ctime()
            try:
                x = timestamp[-1]
                print ('\nLast time you logged in at', x)
            except IndexError:
                pass
            print ('\nYou are logged in\n')
            timestamp.append(tm)
            break
        
def Update():
    user = input(usrnmsg).strip().lower()
    if user not in db:
        print ("\nAccount doesn't exist\n")
    else:
        passwd = input(paswdmsg).strip()
        password = db.get(user)
        if password == passwd:
            passwd1 = input('Enter New password').strip()
            db[user] = passwd1
            print ('\nAccount Updated\n')
        else:
            print ('\nYou are not authorized to change password\n')
        
def Display():
    for i in db:
        print (i)

def Remove():
    quote = input('Enter the Username you want to remove: ')
    db.pop(quote,"Invalid Entry! User Doesn't exists")
    
def ShowMenu():
    prompt = """Select your choice:
(N)ew Account
(O)Login
(U)pdate Password
(Q)uit
(R)emove
(D)isplay

Enter Choice here: """
    while True:
        while True:
            try:
                choice = input(prompt).strip().lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print ('\nYou have chosen: [%s]\n'%(choice))
            if choice not in 'nouqrd':
                print ('\nInvalid Option.Enter Again')
            else:
                break
                    

        if choice == 'n':
            NewAc()
        if choice == 'o':
            OldAc()
        if choice == 'u':
            Update()
        if choice == 'q':
            break
        if choice == 'r':
            Remove()
        if choice == 'd':
            Display()
            
if __name__=='__main__':
    ShowMenu()

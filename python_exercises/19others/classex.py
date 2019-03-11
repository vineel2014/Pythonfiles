class Calculator:

    #x=int(input("Enter an Integer:"))
    #y=int(input("Enter an Integer:"))

    def __init__(self):
         self.x =0
         self.y =0

    def sum(self,x,y):
        print("ADDITION:",x+y)
    def sub(self,x,y):
        print("SUBTRACTION:",x-y)
    def mul(self,x,y):
        print("MULTIPLICATION:",x*y)
    def div(self,x,y):
        if b==0:
            print("DENOMINATOR SHOUD NOT BE ZERO")
        else:
            print("DIVISION:",x/y)
            print("iNTEGER DIVISION:",x//y)
            


c=Calculator()
print("**********AIRTHMETIC CALCU:ATOR***********")

while True:
    #a=int(input("Enter an Integer:"))
    #b=int(input("Enter an Integer:"))
#print("**********AIRTHMETIC CALCU:ATOR***********")
    print("AVAILBLE CHOICES ARE:")
    print("1.ADDITION")
    print("2.SUBTRCTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    ch=int(input("ENTER YOUR CHOICE:"))
    if ch==1:
        a=int(input("Enter an Integer:"))
        b=int(input("Enter an Integer:"))
        c.sum(a,b)
    elif ch==2:
        a=int(input("Enter an Integer:"))
        b=int(input("Enter an Integer:"))
        c.sub(a,b)
    elif ch==3:
        a=int(input("Enter an Integer:"))
        b=int(input("Enter an Integer:"))
        c.mul(a,b)

    elif ch==4:
        a=int(input("Enter an Integer:"))
        b=int(input("Enter an Integer:"))
        c.div(a,b)
    else:
        print("YOU ENTERED WROMG CHOICE ")
     
    s=input("DO YOU WANT TO CONTINUE PRESS Y ")

    if s.equals('Y'):
        continue
    else:
        break
    
    

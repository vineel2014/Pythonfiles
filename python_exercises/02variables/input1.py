from datetime import datetime
a=int(input("enter an integer:"))
print("You Entered:",a,id(a),type(a))
b=float(input("enter a floating point number:"))
print("You Entered:",b,id(b),type(b))
c=input("Enter a character:")
print("You Entered:",c,id(c),type(c))
d=input("enter a string:")
print("You Entered:",d,id(d),type(d))

i = str(input('Enter date in DD/MM/YY:'))
try:
    dt_start = str(datetime.strptime(i, "%d/%m/%y"))[:10]
    print(dt_start,id(dt_start),type(dt_start))
except ValueError:
    print ("Incorrect format")

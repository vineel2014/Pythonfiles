#import math
#from _operator import mod
n=int(input("Enter an Integer:"))
print(n)
s=0
t=n
a=0
print(t)
while (n>0):
    a=n%10
    print("a value:",a)
    s=s+(a*a*a)
    print("s value:",s)
    n=n//10
    print("n value",n)
print(s)   
if(t==s):
    print("Entered number is Amstrong ")
else:
    print("Entered number is not Amstrong")
    
    

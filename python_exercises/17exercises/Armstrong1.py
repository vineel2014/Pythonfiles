#import math
#from _operator import mod
n=int(input("Enter ending Range to print Amstrong numbers:"))
print(n)
a=0
for i in range(1,n+1):
    s=0
    t=i
    while(i>0):
        a=i%10
        s=s+(a*a*a)
        i=i//10
       
    if(t==s):
        print("")
        print("Armstrong numbers:",s)
        

n=int(input("Enter an integer"))
s=0
t=n
print("You entered:",t)
while (n>0):
    a=n%10
    f=1
    for i in range(1,a+1):
        f=f*i
    s=s+f
    n=n//10
print("Result:",s)    
if(t==s):
    print("Entered number is strong")
else:
    print("Entered number is not strong")
    
     
       
    

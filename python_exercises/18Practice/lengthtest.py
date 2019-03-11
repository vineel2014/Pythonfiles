#import linecache
def lengthcalc():
    
    print("Choices:")
    print("")
    print("1:Length of a given string")
    print("")
    print("2:Length of a List")
    print("")
    z=int(input("Enter your choice:"))
    if(z==1):
        print("")
        s=input("Enter a String:")
        a=len(s)
        print("")
        print("Your entered string was:",s)
        print("")
        print("Length of the given String:",a)
    elif(z==2):
        a=[]
        print("")
        x=int(input("Enter the ending range to insert elements into List"))
        for i in range (1,x+1):
            a.append(i)
        print("")
        print("The elements of the given List are: ",a)
        print("")
        print("Length of the given List:",len(a))
    else:
        print("")
        print("your entered choice was wrong")
lengthcalc()
while True:
    #lengthcalc()
    chc=input("Do you want to continue enter yes or no to exit")  
    if(chc=="yes" or chc=="YES"):
        lengthcalc()
    
    elif(chc=="no" or chc=="NO"):
        break
    else:
        print("")
        print("Please enter either yes or no")
        continue
    
    
    
      
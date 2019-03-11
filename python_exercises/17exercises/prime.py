
import datetime
print(datetime.datetime.now())
#num1 = int(input("Input starting number in the range: "))
num = int(input("Input ending number in the range: "))

ctr=0
ctr1=0
for x in range(2,num):
    #print(x,end="*")
    prime = True
    for i in range(2,x):
        ctr1=ctr1+1
        #print("")
        #print(i,end="In 2nd LOOP")
        #print("")
        if (x%i==0):
            prime = False
    if prime == True:
        print("")
        print (x,end=" IS PRIME")
    ctr=ctr+1
print("6i")
print(datetime.datetime.now())    
print("")
print("Inner loop Count:",ctr1)
print("Count:",ctr)
print ("Done......")

def histogram(a):
    k=1
    print("")
    print("Histogram:")
    for k in a:
        #print(k)
        s=k*"*"
        print("")
        print(s)
a=[]
x=int(input("Enter the ending range to insert elements into List"))
for i in range (1,x+1):
    k=int(input("enter the integers into the list"))
    a.append(k)
s=histogram(a)


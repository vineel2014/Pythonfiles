n=int(input("Enter an ending range to print strong numbers"))
for i in range(1,n+1):
    s=0
    t=i
    while (i>0):
        a=i%10
        f=1
        for k in range(1,a+1):
            f=f*k
        s=s+f
        i=i//10
    if(t==s):
        print("")
        print("Strong:",s)
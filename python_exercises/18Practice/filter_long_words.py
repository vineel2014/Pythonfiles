def filter_long_words(a,n):
    d=[]
    for i in range(0,len(a)):
        if (len(a[i])>n):
            d.append(a[i])
    return d
a=[]
y=int(input("enter ending range of list"))
for x in range(1,y+1):
    st=input("enter stings to insert into list")
    a.append(st)
z=int(input("enter an integer"))
k=filter_long_words(a,z)
print("The List strings of length greater than the given integer:",k)


      
        
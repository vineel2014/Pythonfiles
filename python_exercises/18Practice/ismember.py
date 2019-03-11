def is_member(a):
    y=int(input("Enter an integer"))
    #for z in range(len(a)):
    if(y in a):
        return True
    else:
        return False 
            
    
d=[]
x=int(input("enter the ending range of the list"))
for i in range (1,x+1):
    d.append(i)
k=is_member(d)
print("Member in list:",k)

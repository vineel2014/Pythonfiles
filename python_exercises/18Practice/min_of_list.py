def max_of_list(c):
    return min(c)      
print("")
d=[]
x=int(input("Enter the ending range to insert elements into List"))
for i in range (1,x+1):
    k=int(input("Enter the elements into the list"))
    d.append(k)
z=max_of_list(d)
print("")
print("Minimum List Element:",z)
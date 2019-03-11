
def add(a):
    return sum(a)
def mult(c):
    total=1
    for i in range(0,len(c)):
        total*=c[i]
    return total
        
#b=[1,2,3,4]
print("")
d=[]
x=int(input("Enter the ending range to insert elements into List"))
for i in range (1,x+1):
    d.append(i)
print("")
print("The elements of the given List are: ",d)
print("")
print("Sum of list elements are:",add(d))
print()
print("Product of list elements are:",mult(d))   
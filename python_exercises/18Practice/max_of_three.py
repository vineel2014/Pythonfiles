def max_of_3(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    elif z>x and z>y:
        return z
    elif ((x==y) or (y==z) or (x==z)):
        if (not(x==y==z)):
            print("Two numbers are same")
            return max(x,y,z)
        else:
            print("Three numbers are equal")
a=int(input("Enter an integer1:"))
b=int(input("Enter an integer2:"))
c=int(input("Enter an integer3:"))
c=max_of_3(a,b,c)
print("Maximum number:",c)
    
        

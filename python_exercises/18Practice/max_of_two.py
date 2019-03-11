def max_of_two(x,y):
    if x>y:
        return x
    elif x<y:
        return y
    else:
        print("Two numbers are equal")
a=int(input("Enter an integer1"))
b=int(input("Enter an integer2"))
c=max_of_two(a,b)
print("Maximum number:",c)
    
        
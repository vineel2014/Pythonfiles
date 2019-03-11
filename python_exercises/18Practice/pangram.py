def pangram(t):
    a= "abcdefghijklmnopqrstuvwxyz"
    p = ""
    for char in t:
        if char in a:
            p+= char
    for char in a:
        if char not in t:
            print(p,a)
            return False

    return True


   
st=input("enter a string")
b=pangram(st)
print("pangram:",b)
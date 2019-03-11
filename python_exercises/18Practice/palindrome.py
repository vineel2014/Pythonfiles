#from collections import Counter
def is_palindrome(s):
    #print(s)
    x=s
    #print(x)
    y=s[::-1]
    #print(y)
    if y == x:
        return True
    else:
        return False
k=input("enter a string:")
z=is_palindrome(k)
print("Palindrome:",z)

"""
This Program generates n Characters
"""
import sys
import time
def generate_n_chars(n,s):
    return n*s

n=int(input("Enter number of characters required:"))
s=input("Enter a character:")
if len(s) > 1:
    print ("Error! Only 1 character is allowed!")
    print("Sorry You entered a string program is terminating......")
    #time.sleep(10) 
    for i in range(100+1):
        time.sleep(0.1)
        sys.stdout.write(('='*i)+(''*(100-i))+("\r [ %d"%i+"% ] "))
        sys.stdout.flush()
    print("")
    print("program was Terminated")
    sys.exit()
p=generate_n_chars(n,s)
print("")
print(p)

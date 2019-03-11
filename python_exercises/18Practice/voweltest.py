#import re
import time
import sys
#import click

def func(v):
    if (v=='a' or v=='e' or v=='i' or v=='o' or v=='u'):
        return True
    else:
        return False
s=input("Enter a character")
if len(s) > 1:
    print ("Error! Only 1 character allowed!")
    print("Sorry You entered a string program is terminating......")
    #time.sleep(10)
    for i in range(100+1):
        time.sleep(0.1)
        sys.stdout.write(('='*i)+(''*(100-i))+("\r [ %d"%i+"% ] "))
        sys.stdout.flush()
    print("")
    print("program was Terminated")
    sys.exit()
b=func(s)
print("Vowel:",b)
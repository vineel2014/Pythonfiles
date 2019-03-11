#************INTERNET SPEED TEST PROGRAM*********************
# __AUTHOR__: VINEEL KUMAR
# VERSION:1.0
#TESTED OS:LINUX
#************************************************************

#Tested in Python 3 Version
#Run this program with admin Privileges
#You only need to run Main.py It calls other Programs

import os
import time

print ("Current date & time " + time.strftime("%c"))
s=os.system("speedtest-cli --simple")

if s==0:

    import mail
    import sms
else:
    print("Internet was down!")




import sys

import os

import datetime

start=datetime.datetime.now()

print()

print ("You are in ", sys.platform ,"os")

print()

print("Linux OS details:")

os.system("lsb_release -dc")

print()

print ("Current System User:",os.environ['USER'] )                

print()

print ('Current Running file name:', sys.argv[0])

pathname = os.path.split(os.getcwd())[1]

print()

print ('Current Working Directory:', pathname)

print()

print ('full path =', os.path.abspath(pathname))

print()

print("Current System time:",datetime.datetime.now().time())

end=datetime.datetime.now()

et=end-start

print("Program exection time:",et)

import os

total = 0

total1= 0

print()

print ("Current Working Directory:",os.getcwd())

print()

for root, dirs, files in os.walk('.'):
   
     total += len(files)
     
     print()

     print("List of files in a given Directory:",files)

     total1 +=len(dirs)
      
     print()

     print("List of subdirectories in a given Directory:",dirs)

print()

print("Number of subdirectories in a given Directory:",total1)

print()

print("Number of files in a given directory:",total)

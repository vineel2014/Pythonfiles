import os
count = 0
c=0
c1=0

for (dirname, dirs, files) in os.walk('.'):
   for filename in files:

       if filename.endswith('.py') :
           count = count + 1

       elif filename.endswith('.txt') :

           c=c+1

       else:
       
           c1=c1+1

print ('Pyhton Files:', count)

print ('TEXT Files:', c)

print("Others:",c1)

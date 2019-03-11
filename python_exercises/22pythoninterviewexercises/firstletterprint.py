import os

import glob

import sys

os.system("clear")

b=[]

try:

    #for x in glob.glob('*.txt'):

    #b.append(x)


    print()

    print ("Current Working Directory:",os.getcwd())

    print()

    for root, dirs, files in os.walk('.'):

        for name in files:

            if name.endswith('.txt'):        

                b.append(os.path.join( root[len(dirs):], name ))



    print("Files to be opened:",b)

    if b==[]: raise
    
    l = []

    l1=[]

    l2=[]


    #print("Opening file:",a)

    print()

    for k in b:

        #if b==[]: break

        print()

        print("Current opening file:",k)

        print()

        with open(k,'r') as f:

           for line in f:

               l.append(line[0])

        #print first character in each line in a file
       
        for i in l:
       
            if i=='\n':

                continue
    
            else:

                print()
    
                print("Print first letter of each line in the file ",i)

        f.close()
        l.clear()

        print()
        #print first word  in each line in a file

        with open(k,'r') as f:

            for line in f:

                l1.append(line.split(' ', 1)[0]) 

        for i in l1:

            if i=='\n':
       
                continue
            else:
        
                print()
        
                print("Print first word of each line in the file:",i)

        f.close()
        l1.clear()

        print()
    
        # print all lines in a file

        with open(k,'r') as f:

            for line in f:

                l2.append(line)

        for i in l2:

            if i=='\n':
       
                continue
   
            else:
       
                print()
       
                print("Print each line in the file:",i)

        f.close()
        l2.clear()



except:

    print("No Text files found in the given path")


finally:

    print("Successfully done checking Text files in the given path")

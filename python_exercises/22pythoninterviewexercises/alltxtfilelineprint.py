import os

import sys

class allfile:

    def fetch(self):

        print()
        l=[]

        print()

        print ("Current Working Directory:",os.getcwd())

        x=os.getcwd()

        for root, dirs, files in os.walk('.'):

            print()

            print("root;",root)

            for name in files:

                if name.endswith('.txt'):
           
                        l.append(os.path.join( root[len(dirs):], name ))
            #print()
            #print("Text Files in the directory:",l)         
            print()
            print("List of text files in the current working Directory:",l)


            #print each line in every text file in the specified path

            l1=[]

            for i in l:

                print()

                print("Current opening file:",i)

                print()

                with open(i,'r') as f:

                    for line in f:
 
                        l1.append(line)

                for j in l1:

                    if j=='\n':

                        continue

                    else:

                        print()
                        print(j) 

                f.close()
                l1.clear()
            
            l.clear()

s=allfile()
s.fetch()



import os

os.system("clear")

f=input("Enter file name to check weather exists in the current working directory:")

k=os.path.basename(os.getcwd())

for root,dirs,files in os.walk("."):


    if f==k:
    
        print("Given  name is the name of current working directory")
        break

    elif f in dirs:
        print("Given name is a subdirectory in the current working directory")
        break
 
    elif f in files:        

        print("Given file exists in the current working directory")
        break

    else:

        print("Given file or subdirectory not exists in the current working directory")   
        break

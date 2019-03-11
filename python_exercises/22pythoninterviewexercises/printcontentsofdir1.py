import os

path="/home/vineel/pypract/"

os.chdir(path)

for dirpath,dirnames,filenames in os.walk(path):

    print("Current path:",dirpath)
    print("Dirctory names:",dirnames)
    print("File names:",filenames)
    print()


import os

print("Current Working Directory:",os.getcwd())

for dirname,dirnames,filenames in os.walk('.'):

    for subdirname in dirnames:

        print("Subdirectory:",os.path.join(dirname,subdirname))

    for filename in filenames:

        print("Filename:",os.path.join(dirname,filename))


    if '.git' in dirnames:

        dirnames.remove('.git')



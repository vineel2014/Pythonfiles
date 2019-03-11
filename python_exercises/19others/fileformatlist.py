import os,glob

os.chdir("/home/vineel/Downloads/")

#dispays all jpg images in the given path

for file in glob.glob("*.jpg"):
    print(file)

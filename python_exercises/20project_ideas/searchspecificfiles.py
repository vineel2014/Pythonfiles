import fnmatch

import os

import re
 
rootPath = '/'

    
print("Pattern must be like: *.mp3 or *.jpg e.t.c")

pattern = input("Enter pattern to search files:")

#pattern = '*.mp3'

if pattern== '*.mp3' or '*.jpg' or '*.jpeg' or '*.mpeg' or '*.avi' or '*.wav':

    for root, dirs, files in os.walk(rootPath):

        for filename in fnmatch.filter(files, pattern):

            print( os.path.join(root, filename))

else:

    print("It's a non matching pattern")


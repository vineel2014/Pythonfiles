#you need to install youtube -dl in Linux

#Usage: Enter youtube url as input

import os

s=input("Enter you tube url to doenload video:")

try:
    os.system("youtube-dl " + s+ " --verbose")

except:

    print("Error in getting Video information")



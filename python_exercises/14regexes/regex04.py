# Serach & Replace
import re

def main():
    fh = open('raven.txt')
    #print(fh)
    for line in fh:
        print(re.sub('(Len|Neverm)ore','###', line),end='')
    
    fh.close()
    
if __name__ == "__main__": main()

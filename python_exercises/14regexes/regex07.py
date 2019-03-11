import re

def main():
    fh = open('raven.txt')
    pattern = re.compile('(Len|Neverm)ore',re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(line, end='')
    
    fh.close()
    
if __name__ == "__main__": main()

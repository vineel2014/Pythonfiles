import re

def main():
    fh = open('raven.txt')
    i = 0
    for line in fh:
        i += 1
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group(), 'line no = ', i)
            
    fh.close()
    
if __name__ == "__main__": main()

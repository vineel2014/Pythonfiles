def main():
    try:
        #fh = open('xlines.txt')
        fh = open('lines.txt')
    except:
        print('could not open the file')
    else:
        for line in fh: print(line.strip())
        fh.close()
    
    
if __name__ == "__main__": main()

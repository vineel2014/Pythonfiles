def main():
    
    try:
        fh = open('xlines.txt')
        for line in fh: print(line.strip())
        
    except IOError as e:
        print('could not open the file', e)
        

if __name__ == "__main__": main()

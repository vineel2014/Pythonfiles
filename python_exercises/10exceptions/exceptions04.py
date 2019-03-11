def main():
    try:
        for line in readline('xlines.doc'): print(line.strip())
        fh.close()
    except IOError as e:
        print("can't open",e)
    except ValueError:
        print('bad file name')

def readline(filename):
    if filename.endswith('.txt'):
        fh = open('lines.txt')
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .txt')
        

if __name__ == "__main__": main()

def main():
    fin = open('lines.txt','r')
    fout = open('new.txt','w')
    for line in fin:
        print(line, file = fout, end = '')
    print('Done!')

if __name__ == "__main__": main()

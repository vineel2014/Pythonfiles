def main():
    
    fin = open('newBigfile.txt','r')
    fout = open('XnewBigfile.txt','w')
    
    buffersize = 50000
    buffer = fin.read(buffersize)
    
    while len(buffer):
        print('.',end='')
        #print(buffer, file = fout, end = '')
        fout.write(buffer)
        buffer = fin.read(buffersize)
    
    print('Done!')

if __name__ == "__main__": main()

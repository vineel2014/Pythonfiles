def main():
    
    fin = open('olives.jpg','rb')
    fout = open('newOlives.jpg','wb')
    
    buffersize = 50000
    buffer = fin.read(buffersize)
    
    while len(buffer):
        print('.',end='')
        fout.write(buffer)
        buffer = fin.read(buffersize)
    
    print('Done!')

if __name__ == "__main__": main()

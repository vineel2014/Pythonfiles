def main(): 
    s = 'this is a string'
    for i,c in enumerate(s): #print index if c == s
        if c=='s': print('index {} is an s'.format(i))
        
if __name__ == "__main__": main()

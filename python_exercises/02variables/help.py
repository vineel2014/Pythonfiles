def main():
    
    x = [1,2,3]
    print (x,type(x))
    print ('-'*100)
    print ('This is the Dir List', dir(x))
    print ('-'*100)
    print('This is Help:', help(x))
    print ('-'*100)
    print ('This is the Doc String', x.__doc__)

if __name__ == "__main__": main()

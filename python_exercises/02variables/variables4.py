#strings

def main():
    
    x = "This is an \n immutable type object"
    print (x,'\n', type(x))
    
    print()
    
    x = r"This is an \n immutable type object"
    print (x,'\n', type(x))
    
    print()
    
    x = 'Same can be written within single quotes'
    print (x,'\n', type(x))
    
    print()
    
    x = 100
    s = "This string will contain the value {} that belongs to x ".format(x)
    t = "This string will contain the value %d that belongs to x "%(x)
    print (s,'\n', type(s))
    print (t,'\n', type(t))
    
    print()
    
    x = '''\
This is line 1
This is line 2
This is line 3
This is last line.
    '''
    print (x)
    
    print()


if __name__ == "__main__": main()

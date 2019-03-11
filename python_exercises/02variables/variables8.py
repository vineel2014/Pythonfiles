#boolean

def main():
    x = True
    y = True
    
    print (x,'\t',id(x),'\t',type(x))
    print (y,'\t',id(y),'\t',type(y))
    
    print(x == y)
    print(x is y)
    print(id(x)== id(y))
    
    x = False
    y = 0
    
    print (x,'\t',id(x),'\t',type(x))
    print (y,'\t',id(y),'\t',type(y))
    
    print(x == y)
    print(x is y)
    
    x = True
    y = 0
    
    print((x>y))
    print((x>y)+1)
    
    

if __name__ == "__main__": main()

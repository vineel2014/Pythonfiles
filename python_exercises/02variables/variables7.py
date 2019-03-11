# ID is a unique ID that refers to a specific Object:

def main():
    x = 42
    y = 42
    
    print (x,'\t',id(x),'\t',type(x))
    print (y,'\t',id(y),'\t',type(y))
    
    print (x==y)
    print (x is y)
    
    x = dict(a = 42)
    y = dict(a = 42)
    
    print (x,'\t',id(x),'\t',type(x))
    print (y,'\t',id(y),'\t',type(y))
     
    print (x==y)
    print (x is y)
    

if __name__ == "__main__": main()

#numbers

def main():
    x = 42
    print (1,'\t', x,'\t', id(x),'\t',type(x))
    
    x = 42.0
    print (2,'\t', x,'\t', id(x),'\t',type(x))
    
    x = 43/4
    print (3,'\t', x,'\t', id(x),'\t',type(x))
    
    x = 43//4
    print (4,'\t', x,'\t', id(x),'\t',type(x))
    
    x = 43%4
    print (5,'\t', x,'\t', id(x),'\t',type(x))
    
    x = round(43/4)
    print (6,'\t', x,'\t', id(x),'\t',type(x))
    
    x = round(43/4,1)
    print (7,'\t', x,'\t', id(x),'\t',type(x))
    
    x = int(14.77)
    print (8,'\t', x,'\t', id(x),'\t',type(x))
    
    x = float(14)
    print (9,'\t', x,'\t', id(x),'\t',type(x))
    
    
if __name__ == "__main__": main()

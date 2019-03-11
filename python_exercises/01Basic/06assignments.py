def main():
    a = 1
    print(a, type(a), id(a))
    
    a = "two"
    print(a, type(a), id(a))
    
    c,d = 3,4
    print(c,id(c),d,id(d))
    
    c,d = d,c
    print(c,id(c),d,id(d))
    
    e = (1,2,3,4,'a',(1,2),[1,3],3.02)
    print (e, type(e),id(e))
    
    f = [1,2,3,4,'a',(1,2),[1,3],3.02]
    print(f, type(f), id(f))
    
    f[0] = 'b'
    print(f, type(f), id(f))



if __name__ == "__main__": main()

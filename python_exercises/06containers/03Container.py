def main():
    
    t = tuple(range(25,99))
    print (t)
    print (type(t))
    print(10 in t)
    print(50 in t)
    print(50 not in t)    
    for i in t: print(i, end='::')
    print()
    print(t.count(26))
    print(t.index(26),end='.........')
    
    print()
    l = list(range(25))
    print (l)
    print (type(l))
    print(10 in l)
    print(50 in l)
    print(50 not in l)    
    for i in l: print(i, end='xx')
    print()
    l[10]=25
    print (l)
    print(l.count(5))
    print(l.index(5))
    
    l.append('Last Element')
    print(l)
    l.extend(range(20))
    print(l)
    l.insert(12,'Inserted')
    print(l)
    l.remove('Inserted')
    print(l)
    del l[25]
    print(l)
    print(l.pop())
    print(l)
    print(l.pop(10))
    print(l)
    
    
if __name__ == "__main__": main()

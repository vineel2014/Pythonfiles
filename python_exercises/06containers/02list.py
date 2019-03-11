def main():
    l = [1,2,3,4]
    print(id(l))
    print(l)
    print(l[0],l[3], l[-1])
    print(len(l))
    print(min(l))
    print(max(l))
    
    l = list(range(26,100))
    print(id(l))
    print (l)
    l[10]='xxx'
    print (l)

if __name__ == "__main__": main()

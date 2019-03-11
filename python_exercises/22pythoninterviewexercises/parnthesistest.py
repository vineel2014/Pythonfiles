def partest(str):

    print(str)
    
    l=list(str)
    c=0
    c1=0
    for i in l:
        c=c+1
        c1=c1+1
        a=i
        if a=='(':
            print("open paranthesis found at position:",c)
        elif a==')':
            print("close paranthesis found at position:",c1)
        else:
            pass

        print(i)


    #for k in l:

    #   print(l.index(k))
   
    #    print('open paranthesis found')

str=input("Enter string with paranthesis:")

partest(str)


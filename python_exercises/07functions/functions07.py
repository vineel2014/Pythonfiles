def main():
    testfunc(1,2,3,50,60,70,eighty = 80,ninety = 90)

def testfunc(number,another,onemore,*args,**kwargs): #arbitrary numbers of arguments
    print(number,another,onemore,args,kwargs)
    print(number,another,onemore,args,kwargs['eighty'],kwargs['ninety'])

if __name__ == "__main__": main()

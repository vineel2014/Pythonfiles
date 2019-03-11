def main():
    testfunc(1,2,3,50,60,70)

def testfunc(number,another,onemore,*args): #arbitrary numbers of arguments
    print(args,number,another,onemore)
    #print(number,another,onemore,*args)

if __name__ == "__main__": main()

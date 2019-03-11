def main():
    testfunc(1,2,3,50,60,70,eighty = 80,ninety = 90)

def testfunc(number,another,onemore,*args,**kwargs):
    for k in kwargs:
        print (k,kwargs[k])
    for i in args:
        print (i)
    print(number)
    print(another)
    print(onemore)
if __name__ == "__main__": main()

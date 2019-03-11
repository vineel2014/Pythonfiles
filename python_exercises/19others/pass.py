def main():

       print("Welcome")

if __name__=="__main__":main()


def second(x):
    x=6
    print(x)
    return x

a=5
second(a)
print(a)


def third(second,*x):
    second(*x)    

    print()


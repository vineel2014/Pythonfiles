def printTri(n):
    for i in range(1,n+1):
        print(' '.join(str(i)*i))
n=int(input("enter range to display number triangle"))
printTri(n)


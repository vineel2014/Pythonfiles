def printTri(n):
    for i in range(n,0,-1):
        print(' '.join(str(i)*i))
n=int(input("enter range to display number triangle in reverse"))
printTri(n)


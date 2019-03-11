from math import sqrt

for n in range(99, 0, -1):

    print(n)

    root = sqrt(n)

    print(root)

    if root == int(root):

        print (n)

        break        

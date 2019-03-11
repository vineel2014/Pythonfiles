def main():

    i=int(input("ENTER AN INTEGER FOR MULTIPLICATION TABLE:"))
    n=int(input("ENTER AN INTEGER TO DISPLAY MULTPLICATION UPTO THE GIVEN RANGE:"))

    for j in range(1, n+1):

        print(i,'*',j,"={:2d}".format(i * j))
        print("\n")

    print()


if __name__=="__main__":main()



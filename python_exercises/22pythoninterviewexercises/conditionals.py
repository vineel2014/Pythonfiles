
def compare(item1,item2):

    try:

        if item1==item2:

            print()

        else:

            raise ValueError(" ")
    except:

        print("Items must be same type")

    if id(item1)==id(item2):
	
        print("Items are in same object")

    elif (id(item1)!=id(item2)) and item1==item2:

        print("Items have the same value")

    else:

        print("Items are different")


x=input("Enter Input 1:")

y=input("Enter Input 2:")

compare(x, y)

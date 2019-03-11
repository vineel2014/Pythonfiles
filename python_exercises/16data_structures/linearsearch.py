List=[1,2,3,4,5,6]

item=5

position = 0

found = False

while position < len(List) and not found:

    if List[position] == item:

        found = True

    position = position + 1

if found==True:

    print(item," Found at position:",position)

else:

    print(item,"Not Found")

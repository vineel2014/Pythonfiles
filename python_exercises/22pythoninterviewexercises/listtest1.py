list1=[1,2,3,4,5,6,7,8,9,10,11,13,17,18]
list2=[x for x in list1 if ((x%2==0) and (list1[0::2]))]
print("List items at odd index Positions:",list1[1::2])
print("List items at even index Positions:",list1[0::2])
print(list2)


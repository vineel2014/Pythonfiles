#operation1

x=[[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2,3,4,5,6]]

print("Initial List:",x)

c=[]

while x:

    c.extend(x.pop(0))

print("Final List:",c)


print("Enumerated List:",list(enumerate(c)))

print("Remove List duplicate elements:",list(set(c)))


#List inbuilt functions

print("List Elements before deletion at index 2:",c)

del c[2]

print("List Elements After deletion at index 2:",c)


print("List contains",len(c),"Items")









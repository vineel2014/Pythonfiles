def extendList(val, list1=None):
    if list1 is None:
        list1 = []
        list1.append(val)
    return list1

list1 = extendList(10)
list2 = extendList(123)
list3 = extendList('a')

print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)

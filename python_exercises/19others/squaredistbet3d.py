import math
list1=[0.3,0.0,0.4]
list2=[0.2,0.5,0.6]
diff=[]
sqr=[]
a=0.0
for index  in range(len(list1)):
    diff=list1[index]-list2[index]
    sqr=diff*diff
    a+=sqr
    print (diff,sqr)
print(a)



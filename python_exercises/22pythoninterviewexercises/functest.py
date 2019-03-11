def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
        print("LIST IN IMPLEMENTATION:",l)
    print("LIST AFTER IMPLEMENTATION:",l) 

f(2)
f(3,[3,2,1])
f(3)

#See below code for basic understainding

"""l_mem = []

l = l_mem           # the first call
for i in range(2):
    l.append(i*i)

print(l)            # [0, 1]

l = [3,2,1]         # the second call
for i in range(3):
    l.append(i*i)

print(l)            # [3, 2, 1, 0, 1, 4]

l = l_mem           # the third call
for i in range(3):
    l.append(i*i)

print(l)            # [0, 1, 0, 1, 4]

"""

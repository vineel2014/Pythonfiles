#!/usr/bin/python3

l=[]

k={}

#adding dictionary to a list inside for loop
for i in range(1,10):

    l.append({'a':i})

print(l)

l.clear()

keys=[]

for i in range(1,10):

    keys.append('a')

values=[]

for i in range(1,10):

    values.append(i)

#print(values)

k=dict(zip(keys,values))

#print(k) 

#adding dictionary to list outside for loop

l.append(k)

print(l)

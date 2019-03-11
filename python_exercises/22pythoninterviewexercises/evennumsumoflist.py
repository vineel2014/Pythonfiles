x=[1,2,3,4,5]

print("Actual List:",x)

Even=[i for i in x if (i%2)==0]

print("Even numbers in the list:",Even)

c=0

for i in Even:

    c+=i

print("Total of Even numbers in a list:",c)

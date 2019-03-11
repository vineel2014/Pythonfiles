x=[1,2,3,4,5]

print("Actual List:",x)

odd=[i for i in x if (i%2)!=0]

print("Odd numbers in the list:",odd)

c=0

for i in odd:

    c+=i

print("Total of odd numbers in a list:",c)

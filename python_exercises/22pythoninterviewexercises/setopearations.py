l=[1,2,3,4,5]
l1=[1,4,5,6,7]
a=set(l)
b=set(l1)


print("SET1:",a)
print("SET2:",b)

print("UNION (SET1 UNION SET2):",a.union(b))
print("INTERSECTION (SET1 INTERSECTION SET2):",a.intersection(b))
print("DIFFERENCE (SET1-SET2):",a-b)
print("DIFFERENCE (SET2-SET1):",b-a)
print("DIFFERENCE:",a.difference(b))
print("DIFFERENCE:",b.difference(a))
print("SYMMETRIC DIFFERNCE (SET1 ^ SET2):",a^b)
print("SYMMETRIC DIFFERNCE:",a.symmetric_difference(b))
print("NO COMMON ELEMENTS in SET1 and SET2:",a.isdisjoint(b))
print("SET1 IS SUBSET OF SET2:",a.issubset(b))
print("SET1 IS SUPERSET OF SET2:",a.issuperset(b))

c=a.copy()

print("SET3 IS COPY OF SET1:",c)

a.add(6)

print("SET1 AFTER ADDING ELEMENT:",a)

c.clear()

print("SET3 AFTER CLEARING ALL ELEMENTS:",c)


c=a.copy()

print("SET3 BEFORE DISCARDING ELEMENTS:",c)

c.discard(6)

print("SET3 AFTER DISCARDING ELEMENTS:",c)

print("ALL(SET):",all(c))

print("ANY(SET):",any(c))

print("ENUMERATION OF SET:",c)

for i,j in  enumerate(c):

    print(i,":",j)

print("LENGTH OF  SET:",c,"LENGTH:",len(c))

print("MINIMUM ELEMENT OF SET:",c,"LENGTH:",min(c))

print("MAXIMUM ELEMENT OF SET:",c,"LENGTH:",max(c))

print("SORTED SET:",sorted(c))

print("SUM OF ALL ELEMENTS IN THE SET:",sum(c))



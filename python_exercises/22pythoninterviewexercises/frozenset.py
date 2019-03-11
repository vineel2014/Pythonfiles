try:
    l=[1,2,3,4,5]
    l1=[1,4,5,6,7]
    a=frozenset(l)
    b=frozenset(l1)


    print("FROZENSET1:",a)
    print("FROZENSET2:",b)

    print("UNION (FROZENSET1 UNION FROZENSET2):",a.union(b))
    print("INTERSECTION (FROZENSET1 INTERSECTION FROZENSET2):",a.intersection(b))
    print("DIFFERENCE (FROZENSET1-FROZENSET2):",a-b)
    print("DIFFERENCE (FROZENSET2-FROZENSET1):",b-a)
    print("DIFFERENCE:",a.difference(b))
    print("DIFFERENCE:",b.difference(a))
    print("SYMMETRIC DIFFERNCE (FROZENSET1 ^ FROZENSET2):",a^b)
    print("SYMMETRIC DIFFERNCE:",a.symmetric_difference(b))
    print("NO COMMON ELEMENTS in FROZENSET1 and FROZENSET2:",a.isdisjoint(b))
    print("FROZENSET1 IS SUBSET OF FROZENSET2:",a.issubset(b))
    print("FROZENSET1 IS SUPERSET OF FROZENSET2:",a.issuperset(b))

    c=a.copy()
 
    print("FROZENSET3 IS COPY OF FROZENSET1:",c)

    print("ALL(FROZENSET):",all(c))

    print("ANY(FROZENSET):",any(c))

    print("ENUMERATION OF FROZENSET:",c)

    for i,j in  enumerate(c):

        print(i,":",j)

    print("LENGTH OF  FROZENSET:",c,"LENGTH:",len(c))

    print("MINIMUM ELEMENT OF FORZENSET:",c,"LENGTH:",min(c))

    print("MAXIMUM ELEMENT OF FROZENSET:",c,"LENGTH:",max(c))

    print("SORTED FROZENSET:",sorted(c))

    print("SUM OF ALL ELEMENTS IN THE FROZENSET:",sum(c))


    d=frozenset({1,2,3,4,5})

    print(d)

    print('The empty frozen set is:', frozenset())

    person = {"name": "John", "age": 23, "sex": "male"}

    fSet = frozenset(person)

    print('The frozen set for Dictionary:', fSet)

    d.add(6)

    print(d)


except:

    print("You are trying to do invalid opeartion on  frozenset -Not Allowed")

finally:

    print("Note: Frozensets are Immutable sets")

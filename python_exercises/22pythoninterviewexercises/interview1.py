def multipliers():


    return  [lambda x : i * x for i in range(4)]
    

x=[m(1) for m in multipliers()]

print(x)

print ([m(2) for m in multipliers()])


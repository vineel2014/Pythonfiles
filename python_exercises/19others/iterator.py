
list=[1,2,3,4]
it=iter(list)
print(it)
print(next(it))

for x in iter(list):
    print(x,end="")


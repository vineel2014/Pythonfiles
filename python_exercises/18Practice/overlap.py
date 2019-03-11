def overlap(a,b):
    if set(a).intersection(b):
        return True
    else:
        return False
a=[1,2,3,4]
b=[4,5,6,7,8]
d=overlap(a,b)
print("Overlapping:",d)

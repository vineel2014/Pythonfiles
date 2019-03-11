n=int(input("enter the range for pattern to display"))
print ("Pattern C")
for e in range (n,0,-1):
    print((n-e) * ' ' + e * '1')

print ('')
#print ("Pattern D")
#for g in range (n,0,-1):
#   print(g * ' ' + (n+1-g) * '1')

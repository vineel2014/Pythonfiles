
#General List
print("LIST ITERATOR")
a=[1,2,3,4]
print("List:",a)
for i in a:
    print ("List Items:",i)

#List comprahension
print("LIST COMPRAHENSION")
mylist=[x*x for x in range(3)] 
print("List:",mylist)
for i in mylist:
    print("List Items:",i)

print("GENERATOR")
#Generator
def gen():
    mylist=range(3)
    for i in mylist:
        yield i*i

g=gen()
print("Returnded Generator Object:",g)
for i in g:
    print ("List Items:",i)

#This loop cannot run because generator is empty
for k in g:
    print ("List Items:",k)

#print("Generator:",g)
print(g,":contains no values")

#you need to call function again to get new genator object with values

h=gen()
print("Returnded Generator Object:",h)
for i in h:
    print ("List Items:",i)



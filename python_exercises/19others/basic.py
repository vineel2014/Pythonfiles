print("******First*******")
print("")
def main():
    print("*******In main Function*******")
    print ("Welcome to Python")
print("")
def second():
    print("*******In Function*******")
    print("Second function")
print("")
print ("*******Outside Function******")

#main()
if __name__=="__main__":main()

#else:
 #   print("Main function is not defined")

#if __name__=="__second__":
print("")
second()
print("")
x=input("Enter any value:")
print(x,id(x),type(x))

print("")
y=int(input("Enter an integer:"))
z=int(input("Enter an Integer:"))
print("")
print(y,id(y),type(y))
print(z,id(z),type(z))

s=y+z
print("")
print("SUM:",s)

x=int(x)
if (x>y) & (x>z):
    print(x," is greater than",y,z)

elif (y>x) & (y>z):
    print(y, "is greater",x,z)

elif (z>x) & (z>y):
    print(z ,"is greater",x,y)

elif (x==y):
    print(x ,"and", y ,"are Equal")

elif (y==z):
    print(y," and ", z, " are Equal")

elif (z==x):
    print(z," and ",x," are Equal")

else:
    print(x,y,z, " are Equal")

#x=int(x)
print("")

print("******EVEN NUMBERS BETWEEN 1 AND 10********")
for i in range(0,10,2):
    print(i,end=" ")
else:
    print()
    print("RANGE OVER")
print("")
print("*******ODD NUMBERS BETWEEN 1 AND 10********")
for c in range(1,11,2):
    print(c,end=" ")
else:
    print()
    print("RANGE OVER")

print("")

print("*****REVERSE FOR LOOP*******")

for b in range(10,0,-1):
    print(b,end=" ")

print("")
w=5
print("******WHILE LOOP******")
while w>0:

    print(w,end=" ")
    w-=1
print("")
print("******PASS LOOP******")

for i in range(1,5):
    pass
print("")

print("")
print("*******LIST ITERATOR*****")
l=[1,2,3,4]
print("LIST:",l)
for z in l:
    print()
    print("LIST ITEMS:",z)
    print()

print("")
print("*******TUPLE ITERATOR*****")
l=(1,2,3,4)
print("TUPLE:",l)
for z in l:
    print()
    print("TUPLE ITEMS:",z)
    print()

print("")
print("*******DICTIONARY ITERATOR*****")
l={1:"ONE",2:"TWO",3:"THREE",4:"FOUR"}
print("DICTIONARY:",l)
for key,value in l.items():
    print()
    print("DICTIONARY KEY:",key,"VALUE:",value)
    print()

print("")
print("*******SET ITERATOR*****")
l={1,2,3,4,5,6,7,8,9,0,1,2}
print("SET:",l)
for z in l:
    print()
    print("SET ITEMS:",z)
    print()

print("")
print("*******INTEGER STACK*****")

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)
         return self.items

     def pop(self):
         return self.items.pop()

     def top(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s = Stack() #creates an object

print()

if s.isEmpty(): 
    print("STACK IS EMPTY")

c=0
j=0
while True:
    i=int(input("ENTER INTEGER STACK ITEM:"))
    j=s.push(i)
    print(j)
    c+=1
    if c>=5:
        break
print()
print("STACK TOP",s.top())
l=s.size()
print()
print("STACK SIZE:",l)
print()
print("STACK ITEMS:")
print()
m=0
#h=s
while(l>0):
    try:
        m=s.pop()                
        print(m,"->",end=" ")
        #print(h-1)
    except:
        print()
        print("STACK IS EMPTY")
        break



print("")
print("******* INTEGER QUEUE*****")
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
        return self.items

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q= Queue()

print()

if q.isEmpty(): 
    print("QUEUE IS EMPTY")

c=0
h=0
while True:
    i=int(input("ENTER INTEGER QUEUE ITEM:"))
    h=q.enqueue(i)
    print(h)
    c+=1
    if c>=5:
        break
print()
l=q.size()
print()
print("QUUE SIZE:",l)
print()
print("QUEUE ITEMS:")
print()
n=0
#k=q
while(l>0):
    try:
        n=q.dequeue()
        print(n,"->",end=" ")
        #print(k-1)
    except:
        print()
        print("QUEUE IS EMPTY")
        break


print("")
print("*******LINKED lIST*****")


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head = None
        self.curr = None
        self.tail = None

    def __iter__(self):
        return self

    def next(self):
        if self.head and not self.curr:
            self.curr = self.head
            return self.curr
        elif self.curr.next:
            self.curr = self.curr.next
            return self.curr
        else:
            raise StopIteration

    def append(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = self.tail.next


# Add 5 nodes
ll = LinkedList()
for i in range(1, 6):
    ll.append(i)

# print out the list
while(ll):
    try:
        print(ll.next(),"->",end=" ")
    except:
        print()
        print("LINKED LIST END")
        break


print("*******Last*********")


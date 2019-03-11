
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
    try:
        print()
        i=int(input("ENTER INTEGER QUEUE ITEM:"))
        h=q.enqueue(i)
        print(h)
        c+=1
        if c>=5:
            break
    except:
        print("Wrong Input Given")
        continue

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


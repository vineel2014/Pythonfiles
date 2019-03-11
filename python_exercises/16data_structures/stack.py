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
    try:
        print("")
        i=int(input("ENTER INTEGER STACK ITEM:"))
        j=s.push(i)
        print(j)
        c+=1
        if c>=5:
            break
    except:
        print("Wrong input given")
        continue
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


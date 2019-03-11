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
print()
print("LINKED LIST ITEMS:")
print()

while(ll):
    try:
        print(ll.next(),"->",end=" ")
    except:
        print()
        print("LINKED LIST END")
        break


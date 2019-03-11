

from pythonds import Stack

s = Stack()

for i in range(1000):
    s.push(i)
while s:
    
       k= s.pop()
       print(k)
       if k==0:
           break
        
# which could also be done as:
s = StackFromSequence(range(1000))
while s:
    try:
        print s.pop()
    except:
        print "Stack EMPTY"
# or a little different
s = StackFromSequence(range(1000))
print s.as_tuple()
print s.as_list()


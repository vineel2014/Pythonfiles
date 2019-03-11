
import collections

c = collections.Counter()

print('Initial :',c)

c.update('abcdaab')

print('Sequence:',c)

c.update({'a':1,'d':5})

print('Dict:',c)


#to get and print counter values
c = collections.Counter('abcdaab')

for letter in 'abcde':

    print ('%s:%d'% (letter, c[letter]))


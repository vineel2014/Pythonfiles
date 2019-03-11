#Note:don't maintain two file with same name while using deep copy in the same path

from copy import deepcopy
import copy

lst1 = ['a','b',['ab','ba']] 

#shallow copy

lst2=copy.copy(lst1)

#deepcopy duplicates the itens

lst3 = deepcopy(lst1)
 
print("First List:",lst1)

print("After Shallow Copy:",lst2)

print("After Deep Copy:",lst3)

lst2[2]='c'

lst3[2]='d'


print("After Shallow Copy updating list:",lst2)

print("After Deep Copy updating list:",lst3)

print("First List:",lst1)


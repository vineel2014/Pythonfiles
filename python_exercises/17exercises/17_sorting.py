#Selection Sort. O(n^2)
def Bubble(L):
    length = len(L)
    for i in range(length):
        for j in range(i,length):
            if L[i] < L[j]:
                L[i],L[j] = L[j],L[i]
    print L

def SelSort(L): 
    x = len(L)-1
    for i in range(x):
        index = i
        val = L[i]
        j = i+1
        while j < len(L):
            if val > L[j]:
                index = j
                val = L[j]
            j += 1
        L[i],L[index] = L[index], L[i]
        print L            
            
            

# Merge Sort
def MergeSort(L, lt):
    length = len(L)
    if length<2:
        return L[:]
    else:
        mid = int(length/2)
        left = MergeSort(L[:mid],lt)
        right = MergeSort(L[mid:],lt)
        return Msort(left,right,lt)
    
def Msort(left,right,lt = lambda x,y: x<y):
    result = []
    lenL = len(left)
    lenR = len(right)
    i,j = 0,0
    while i<lenL and j <lenR:
        if lt(left[i],right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i<lenL:
        result.append(left[i])
        i += 1
    while j <lenR:
        result.append(right[j])
        j += 1
    return result

#Sort by Last Names:
def LastNameSort(n1,n2):
    n1 = n1.split(' ')
    n2 = n2.split(' ')
    if n1[0] != n1[0]:
        return n1[0] < n2[0]
    else:
        return n1[1] < n2[1]


    

        
        
            
    

                
            
            
        

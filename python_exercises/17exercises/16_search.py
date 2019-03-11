# Search element in a sorted list
def search(list1,elem):
    return bsearch(list1,elem,0,len(list1)-1)
def bsearch(list1,elem,low,high):
    if (high - low) < 2:
        if list1[high] == elem:
            print 'position = ',high+1
        elif list1[low] == elem:
            print 'position = ',low+1
        else:
            print 'element is not present'
        return
    mid = low + (high - low)/2
    if list1[mid] == elem:
        print 'position = ',mid
        return
    elif list1[mid] < elem:
        return bsearch(list1,elem,mid+1,high)
    elif list1[mid] > elem:
        return bsearch(list1,elem,low,mid-1)

            
    
    

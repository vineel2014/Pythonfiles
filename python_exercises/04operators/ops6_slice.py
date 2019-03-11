def main():
    
    list1 = [1,2,3,4,5,6,7]
    
    print(list1[0])
    print(list1[4])
    #print(list[7])
    print(list1[-1])
    print(list1[0:5])
    
    print('*'*100)
    
    list2 = []
    list2[:] = range(100)
    
    #for i in range(100):
        #list2.append(i) 
        
    print(list2)
    
    print('*'*100)
    
    print (list2[27])
    print (list2[27:42])
    print (list2[27:42:2])
    
    list2[0:20:5] = 'AAA','AAA',"AAA",'AAA'
    print (list2)
    print (list2[0:20:5])
    
if __name__ == "__main__": main()

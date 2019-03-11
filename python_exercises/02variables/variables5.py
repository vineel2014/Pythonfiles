#sequence types

def main():
#     x = (1,2,3)
#     print (x[0])
#     #x[0] = 5
#     print (x,'\t',id(x),'\t',type(x))
#     
#     print()
    
#     x = [1,2,3]
#     print (x[0])
#     x[0] = 5
#     x.append(8)
#     x.insert(3,7)
#     print (x,'\t',id(x),'\t',type(x))
#     
#     print()
#     
    x = 'string'
    print (x[2],'\t',id(x),'\t',type(x))
    print (x[2:4],'\t',id(x),'\t',type(x))
    
    print()
    
    #sequence types are iterables:
    x = (1,2,3,4,5)
    for i in x:
        print(i, end = 'XXXXXX')
        
if __name__ == "__main__": main()

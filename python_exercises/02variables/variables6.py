#dictionary
def main():
    x = {'one':1,'two':2,'three':3,'four':4,'five':5}
    print (x,'\t',id(x),'\t',type(x))
    
    for k in x:
        print(k,x[k])
    
    for k in sorted(x.keys()):
        print(k,x[k])
    
    print ()
    
    x = dict(
        a=1, b=2, c=3, d=4, e=5
    )
    
    x['a'] = 0
    
    for k in sorted(x.keys()):
        print(k,x[k])
        
if __name__ == "__main__": main()

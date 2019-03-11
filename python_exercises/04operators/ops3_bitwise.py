def main():
    
    x = 5
    y = 8
    a = x|y
    b = x&a
    c = x^a #(a & not b)|(not a & b) - EXCLUSIVE OR (if both vale same then 0)
    d=x<<2
    e=x>>2
    f = ~x #compliment operator -(num+1) 
    
#     print(int('00000001101',2))

    print (x,'\t',binary(x))
    print (y,'\t',binary(y))
    
    print()
    
    print (a,'\t',binary(a))
    print (b,'\t',binary(b))
    
    print()
    
    print (c,'\t',binary(c))
    print (d,'\t',binary(d))
    print (e,'\t',binary(e))
    print (f,'\t',binary(f)) 
    
def binary(n):
    binary = ('{:08b}'.format(n))
    return binary

   
if __name__ == "__main__": main()



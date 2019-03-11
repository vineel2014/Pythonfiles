def main():
    testfib(100)
    
x = {0:1, 1:1}
def fib(n):
    assert type(n) == int and n>=0
    if n in x:
        return x[n]
    else:
        x[n] = fib(n-1) + fib(n-2)
        return x[n]
        
def testfib(n):
    for i in range(n+1):
        print ( 'fib of',i,'is',fib(i))
      
if __name__ == "__main__": main()
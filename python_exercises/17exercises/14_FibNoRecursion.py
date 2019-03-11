def main():
    # simple fibonacci series
    # the sum of two elements defines the next set
    a, b = 0, 1
    fib1 = []
    n = 100
    while True:
        fib1.append(b)        
        if len(fib1) > n:
            break
        else:
            a, b = b, a + b
    print(fib1[-1])

if __name__ == "__main__": main()

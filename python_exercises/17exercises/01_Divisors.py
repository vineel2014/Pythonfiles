def main():
    
    x = 3451
    y = 0
    divisors = ()
    for i in range(1,(x//2)+1):
        if not x%i:
            divisors += (i,)
        y += 1
    
    print (divisors,y)

if __name__ == "__main__": main()
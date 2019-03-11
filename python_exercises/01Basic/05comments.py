import datetime
"""Prime numbers till 100
ctr=0
ctr1=0
ctr2=0"""

def main():
    for n in primes(): #generates a list of prime numbers
        if n > 100: break
        #ctr=ctr+1
        print("")
        print(n,end="")

def isprime(n):
    if n == 1: #one is not a prime
        return False
    for x in range(2, n):
        #ctr1=ctr1+1#print(x)
        if n % x == 0:
            return False #found a divisor, not a prime
    else:
        return True

def primes(n = 1):
    while(True):
        if isprime(n): yield n #yield makes it a generator
        n += 1 
print("")
print(datetime.datetime.now())
print("")
if __name__ == "__main__": main()
print("")
print(datetime.datetime.now())


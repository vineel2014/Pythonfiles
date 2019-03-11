def main():
    print(nrt(4,27,0.01))
    
#Nth root of a real number using "BiSection"
def nrt(pwr,val,epsilon):
    assert type(pwr)==int and type(epsilon)==float
    assert (pwr>0 and epsilon > 0)
    if isEven(pwr) and val<0:
        print ("we don't deal with an imaginary number")
        return
    high = max(abs(val), 1.0)
    low = -abs(val)
    guess = (high + low)/2.0
    while abs(guess**pwr - val) >= epsilon:
        if guess**pwr > val:
            high = guess
        if guess**pwr < val:
            low = guess
        guess = (low + high)/2.0

    return guess

def isEven(x):
    return x%2==0
        
      
if __name__ == "__main__": main()
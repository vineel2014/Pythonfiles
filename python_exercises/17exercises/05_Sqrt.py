#Square Root - Bi-section'

def sqrt1(x,epsilon):
    assert x>0,'input should be greater than 0'
    low = 0.0
    high = max(1.0,x)
    ans = (low+high)/2.0
    count = 0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 > x:
            high = ans
        else:
            low = ans
        ans = (low+high)/2.0
        count += 1
    print (ans, 'is the sqrt of', x, count)
        
sqrt1(1000000,.0001)
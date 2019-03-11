text=float(input('Number?'))

if text<0.0:
    print("Number must be positive")
    exit()


if text < 1.0:
    lower=text
    upper=1.0
else:
    lower=1.0
    upper=text

tolerance=1.0e-15


uncertainity=upper-lower
while uncertainity > tolerance:
    middle=(lower+upper)/2.0
    if middle**2 < text:
        lower=middle
    else:
        upper=middle
    #print(lower,upper)
    uncertainity=upper-lower
print(lower,upper)

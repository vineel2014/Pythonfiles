lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

x=0
y=0
for num in range(lower,upper + 1):
    # initialize sum
    s = 0
    x=x+1
    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        s += digit ** 3
        temp //= 10
        y=y+1

    if num == s:
        print(num)
print("Outer Loop Iterations:",x)
print("Inner Loop Iterations:",y)

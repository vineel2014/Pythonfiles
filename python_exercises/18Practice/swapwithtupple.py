x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
x,y= y,x

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
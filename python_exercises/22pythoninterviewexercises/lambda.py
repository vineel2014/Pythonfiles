#Normal function

def square( x):

    #print(x**2)

    print(x,":SQUARE WITHOUT USING LAMBDA:",x ** 2)

#lambda od single line function 

sqre=lambda y:y ** 2


x=int(input("Enter any Integer to find Square:"))

y=x

square(x)

print(y,":SQUARE USING LAMBDA:", sqre(y))




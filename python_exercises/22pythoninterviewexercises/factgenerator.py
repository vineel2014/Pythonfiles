#Factorial program using Generators

def factorial(n):
    count = 1
    fact = 1
    while count <= n:
        yield fact
        #print(fact)
        count = count + 1
        #print(count)
        fact = fact * count
        #print(fact)
    
print ("Factorial program using generators.")
for i in factorial(5):
    print (i)



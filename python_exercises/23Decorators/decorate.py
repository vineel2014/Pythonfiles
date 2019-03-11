def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

x=int(input("Enter any Integer"))
y=int(input("Enter any Integer"))

c=divide(x,y)

print("Result:",c)

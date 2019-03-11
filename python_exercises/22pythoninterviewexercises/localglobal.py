#function for showing local variable

def fun(a):

   a=10

   print ("IN FUNCTION VALUE:",a)

a=20

fun(a)

print ("OUTSIDE FUNCTION VALUE:",a)


#functio showing global variable


def fun1():

    global b
    
    print("IN FUNCTION VALUE BEFORE ASSIGNMENT:",b)
    
    b=10

    print ("IN FUNCTION VALUE AFTER ASSIGNMENT:",b)



b=20

fun1()

print ("OUTSIDE FUNCTION VALUE:",b)



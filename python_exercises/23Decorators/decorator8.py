def decorator_func(original_func):


    def wrapper_func(*args,**kwargs):

        print("Wrapper function can be exected before {}".format(original_func.__name__))

        return original_func(*args,**kwargs)

    return wrapper_func

@decorator_func
def display():

    print("Display function ran")


@decorator_func
def display_info(name,age):

    print("Display function ran with arguments ({},{})".format(name,age))

display_info("vineel",33)

display()








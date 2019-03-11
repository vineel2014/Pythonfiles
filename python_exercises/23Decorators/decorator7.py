def decorator_func(original_func):


    def wrapper_func():

        print("Wrapper function can be exected before {}".format(original_func.__name__))

        return original_func()

    return wrapper_func

@decorator_func
def display():

    print("Display function ran")


display()








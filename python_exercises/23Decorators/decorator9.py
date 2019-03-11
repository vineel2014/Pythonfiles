"""def decorator_func(original_func):


    def wrapper_func(*args,**kwargs):

        print("Wrapper function can be exected before {}".format(original_func.__name__))

        return original_func(*args,**kwargs)

    return wrapper_func"""

#class decorator
class decorator_class(object):

    def __init__(self,original_func):

        self.original_func = original_func


    def __call__(self,*args,**kwargs):

        print("call method can be exected before {}".format(self.original_func.__name__))

        return self.original_func(*args,**kwargs)


@decorator_class
def display():

    print("Display function ran")


@decorator_class
def display_info(name,age):

    print("Display function ran with arguments ({},{})".format(name,age))

display_info("vineel",33)

display()








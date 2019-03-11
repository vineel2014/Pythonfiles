def decorator_func(original_func):


    def wrapper_func():

        return original_func()

    return wrapper_func


def display():

    print("Display function ran")


decorator_display=decorator_func(display)

decorator_display()








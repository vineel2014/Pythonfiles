def decorator_func(msg):


    def wrapper_func():

        print(msg)

    return wrapper_func


hi_func=decorator_func('Hi')
bye_func=decorator_func('Bye')

hi_func()
bye_func()





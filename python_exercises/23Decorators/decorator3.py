def outer_func(msg):


    def inner_func():

        print(msg)

    return inner_func


hi_func=outer_func('Hi')
bye_func=outer_func('Bye')

hi_func()
bye_func()





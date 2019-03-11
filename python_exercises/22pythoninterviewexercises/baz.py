global a
a=0
class Foo(object):

    def bar(self):
        a=10
        print("Before Monkey Patch:",a)


def monkey_bar(self):
    a=20
    print("After monkey Patch:",a)



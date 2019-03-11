import baz

new_obj = baz.Foo()

new_obj.bar()

baz.Foo.bar = baz.monkey_bar

new_obj = baz.Foo()

new_obj.bar()

def our_decorator(func):
    def func_wrap(x):
        print("before calling "+ func.__name__)
        func(x)
        print("after calling "+ func.__name__)
    return func_wrap

def foo(x):
    print("hi, foo has been called with "+str(x))

print("we called foo before decoration: ")
foo("hi")

print("we now decorate foo with f: ")
foo=our_decorator(foo)

print("we now call our decoration: ")
foo(42)
def decorater1(func):
    def wrapper():
        print("Decorator1")
        func()
    return wrapper
def decorater2(func):
    def wrapped():
        print("Decorator2")
        func()
    return wrapped
@decorater1
@decorater2
def say_hello():
    print("hello decoratores")
say_hello()


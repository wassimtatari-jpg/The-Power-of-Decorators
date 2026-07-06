def method_call(func):
    def wrapper(self,*arg,**kwarg):
        print(func.__name__)
        return func(self,*arg,**kwarg)
    return wrapper

class myclass:
    @method_call
    def say_hello(self):
        print("hello my class")
obj=myclass()
obj.say_hello()



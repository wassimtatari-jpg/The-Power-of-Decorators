def log_call(func):
    def wrapper(*arg,**kwarg):
        print(f"calling fucation {func.__name__} and add the elements {arg} the total is :")
        return func(*arg,**kwarg)
    return wrapper
@ log_call
def add(a,b):
    return a+b
print(add(17,88))
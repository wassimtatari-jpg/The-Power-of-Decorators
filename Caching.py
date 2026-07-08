def cache(func):
    resul_cache={}
    def wrapper(*arges):
        if arges in resul_cache:
            return resul_cache[arges]
        result=func(*arges)
        resul_cache[arges]=result
        return result
    return wrapper
@cache
def fib(n):
    if n<2:
        return n
    return fib (n-1)+(n-2)
print(fib(35))
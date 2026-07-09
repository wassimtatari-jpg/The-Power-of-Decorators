import time

def time_decourator(func):
    def wrapper(n):
        start_time=time.time()
        result=func(n)
        end_time=time.time()
        print(f"Execaution time is {end_time-start_time}seconds")
        return result
    return wrapper
@ time_decourator
def compute_square(n):
    time.sleep(2)
    return n*n
compute_square(25)

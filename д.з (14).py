#1
# i don`t know
#2
def chek_annotations(func):
    def wrap(a,b):
        print(func.__annotations__)
        c = func(a,b)
        return c
    return wrap
@chek_annotations
def main(a: str, b: int) -> str:
    return a * b
print (main('hi',10))
#3
from functools import wraps
def cache3(func):

    @wraps(func)
    def wrapper():

        if wrapper.count > 2 or wrapper.count == -1:
            wrapper.cache = func()
            print(wrapper.count)
            wrapper.count = 0
        wrapper.count += 1
        return wrapper.cache

    wrapper.cache = None
    wrapper.count = -1

    return wrapper


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
print(heavy())
#1
def square(num):
    return num**2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = [square(num) for num in numbers if num > 5]
print(squared_numbers)

#2
a = [i for i in range(1,20) if not i % 2 ]
print(a)

#3
def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b
print(list(fib(10))  )

#4
import random
for i in range(4, 15):
    y = random.randrange(9)
    print(y)
    
#5
for line in input('введите:').split(' '): print(line)
#6
def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))
print(random_color())

#7
def find_primes(n):
    primes = []
    for num in range(2, n+1):
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes
n = int(input("Введите число: "))
print("Простые числа в диапазоне от 1 до", n, ":", find_primes(n))

#8
import itertools
def foo(l):
     yield from itertools.product(*([l] * 3))
for x in foo('abcnv'):
     print(''.join(x))
     
#9
def permutations(iterable):
    if len(iterable) == 1:
        yield (iterable[0],)
    else:
        for perm in permutations(iterable[1:]):
            for i in range(len(iterable)):
                yield perm[:i] + (iterable[0],) + perm[i:]
def unique_permutations(iterable):
    return list(set(permutations(iterable)))
print(list(map(list, unique_permutations([1, 1, 1, 0]))))

#10
import random
print(''.join([random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) for i in range(int(input('Количество символов ')))]))

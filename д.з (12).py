#1
my_list = [3, 7, 4, 1, 2]
f = list(filter(lambda x: (x % 2 == 0), my_list))
print(f)
#2
add_numbers = lambda x, y: x + y
print(add_numbers(3, 4))
#3
words = ['ap', 'banana', 'cherry', 'date']
long_words = list(filter(lambda word: len(word) >= 3,words))
print(long_words)
#4
lst=[3,8,6]
sqrs= list(map(lambda x:x**2,lst))
print (sqrs)
#6
words_nums = [8, 1000, 29, 3]
nums = list(filter(lambda number: number >= 10,words_nums))
print(nums)
#7
my_string = 'apples,banana,cherry'
f = lambda x: x.upper()
upper_string = f(my_string)
print(upper_string)
#8
my_list = [3, 7, 18, 9, 2]
f = list(filter(lambda x: (x % 3 == 0), my_list))
print(f)
#9
my_list = [3, 7, 18, 9, 2]
f = list(filter(lambda x: 5<x<10, my_list))
print(f)



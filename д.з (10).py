#1
def summa(a:int,b:int,c:int) -> str :
    v = a * a,b*b,c*c
    return v
print(summa(1, 2, 3))
#2
words = ['fire','gigachad','rapor','jjkfg']
def long_words(words):
    long_words = []
    for word in words:
        if len(word) == 5:
            long_words.append(word)
    return long_words
print(long_words(words))

#3
def get_only_evens(nums) :
    return [i for i in nums[::2] if not i%2]
#4
#5
def only_a(starting_list):
    i = 'a'
    final_list = []

    for char in starting_list:
        if i in char:
            final_list.append(char)
    return final_list
t_string_list = ['apples', 'anytime', 'pop music', 'Never']
print(only_a(t_string_list))
#6
#7
def list_e(starting_list):
    i = 'e'
    final_list = []

    for char in starting_list:
        if i in char:
            final_list.append(char)
    return final_list
t_string_list = ['iphon', 'anywhere', 'pop music', 'Never']
print(list_e(t_string_list))
#8
def all_even(lst):
    for i in lst:
        if i % 2 != 0:
            return False
    return True
#9

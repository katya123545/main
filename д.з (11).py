#1
def prime_number(number) :
    a = 0, 1, 2, 3, 4, 5 #?
    if number in a:
        print('специальное')
    else:
        print('нет')
#2
vowelletters = ("a","e","i","o","u")
def countvowel(word) :
    word = word.lower()
    vowels = [char for char in word if char in vowelletters]
    return len(vowels)
print(countvowel('halodk, doidqj, kqwdk'))
#3
import random
pas = ''
for x in range(16):
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
print(pas)
import random
pas = ''
for x in range(16):
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
print(pas)
import random
pas = ''
for x in range(16):
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
print(pas)
# через def не получилось
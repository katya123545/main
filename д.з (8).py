#1
b = str(input('введите:')).lower()
match b :
    case 'a'|'e'|'y'|'u'|'i'|'o' :
        print('согласная')
    case _:
        print('гласная')

#2
b = str(input('введите:')).lower()
match b :
    case 'суббота'|'воскресенье':
        print('выходной')
    case _:
        print('рабочий')

#3
b = str(input('введите:')).lower()
match b :
    case 'банан'|'лимон':
        print('желтый')
    case 'авокадо'|'киви'|'груша':
        print('зеленый')
    case ('яблоко') :
        print('красный')
    case _:
        print('ощибка')
#4
b = int(input('введите:'))
match b :
    case 1:
        print('ужс')
    case 2:
        print('очень плохо')
    case 3:
        print('ну норм')
    case 4:
        print('почти отличник')
    case 5:
        print('отличник')
    case _:
        print('ощибка')
#list
#1
a = int(input('введите:'))
b = int(input('введите:'))
f=0
i=a
while i<=b:
    f+=i*i
    i+=1
    print(f)
#2
n1 = int(input('ddtlbnt:'))
n2 = int(input('ddtlbnt:'))
print(*[i for i in range(n1, n2 + 1) if i % 2 == 0])
#3
text = input('ddtlbnt:')
vowels = 'уеыаоэяию'
for letter in text:
    if letter in vowels:
        print(letter, end=" ")
print()
#4
for i in range(100): # Numbers between 0 and 100
    if i % 3 == 0 and i % 5 == 0:
        # If i is divisible by 3 and i is also divisible by 5 then print it
        print(i)
#5
l = []
for x in range(6, 102, 5):
  l.append([y for y in range(x-5, x)])
#1
a = input('введите число:')
if len(a) == len(set(a)) :
    print(f'да, это число {a}')
else:
    print('no')
#2
a = input('введите:')
print (a != '')
#3
a = int(input("Введите число : "))
b = str(a)
b1= b + b
b2 = b + b + b
c = a + int(b1) + int(b2)
print("Результат равен:", c)
#4
a = {"школа": "математика"}
a["расстояние до школы"] = 500
a[("любимый предмет")] =['никакой']
print(a["школа"])
del a['любимый предмет']
print(a.keys())
#5
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)

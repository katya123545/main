#1
a = input(str())
b = tuple(a)
c = list(a)
print(b)
print(c)

#8
print("Длины сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

lol = ''
if a + b > c:
    if a + c > b:
        if b + c > a:
            print("Треугольник есть")
        else:
            lol = 'a'
    else:
        lol = 'b'
else:
    lol = 'c'

if lol != '':
    print("Треугольника нет")

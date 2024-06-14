#1
s = input()

length = len(s)
integers = []
i = 0

while i < length:
    s_int = ''
    while i < length and '0' <= s[i] <= '9':
        s_int += s[i]
        i += 1
    i += 1
    if s_int != '':
        integers.append(int(s_int))

print(integers)
#2
a = int(input('Введите число'))
m = a%10
a = a//10
while a > 0:
    if a%10 > m:
        m = a%10
    a = a//10
print(m)
#3
sentence = "is2 Thi1s T4est 3a"
new = " ".join(t[1] for t in sorted([(int(l), w) for w in sentence.split() for l in w if l.isdigit()], key=lambda t: t[0]))
print(new)
#4
def count_users_by_age(users):
    age_count = {}
    for user in users:
        age = user.get('age')
        if age in age_count:
            age_count[age] += 1
        else:
            age_count[age] = 1
    result = [{'age': age, 'count': count} for age, count in age_count.items()]
    return result
users_list = [
    {'age': 25, 'name': 'Вася'},
    {'age': 30, 'name': 'Петя'},
    {'age': 25, 'name': 'Женя'},
    {'age': 30, 'name': 'Егов'},
    {'age': 35, 'name': 'Антон'},
]
result = count_users_by_age(users_list)
print(result)
#5

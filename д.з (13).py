#1
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
sum = 0
for i in matrix:
    for elem in i:
        sum += elem
print("Сумма элементов матрицы:", sum)
#2
d = '13/05/2024'
print(d[-4:] + d[3:5] + d[:2])


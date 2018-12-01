#!/usr/bin/python3

matrix = []
stringIn = str(input())
while stringIn != 'end':
    row = stringIn.split(' ') 
    for j in range(0, len(row), 1):
        row[j] = int(row[j])
    matrix.append(row)
    stringIn = str(input())

n, m = len(matrix), len(matrix[0])

for i in range(0, n, 1):
    for j in range(0, m, 1):
        summa = matrix[i - 1][j] + matrix[i][(j + 1) % m ] + matrix[(i + 1) % n][j] + matrix[i][j - 1]
        print(summa, end=' ')
    print()

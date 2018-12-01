#!/usr/bin/python3

s = str(input())

arraysOfNumbers = s.split()

i = 0
out = ''

if len(arraysOfNumbers) == 1:
    print(s)
else:
    while i < len(arraysOfNumbers):
        leftNeighbor = i - 1
        rightNeighbor = i + 1
        if rightNeighbor == len(arraysOfNumbers):
            rightNeighbor = 0
        sum = int(arraysOfNumbers[leftNeighbor]) + int(arraysOfNumbers[rightNeighbor])
        out = out + str(sum) + ' '
        i += 1
    print(out)

#!/usr/bin/python3

s = str(input())

arraysOfNumbers = s.split()
summa = 0
i = 0

while i < len(arraysOfNumbers):
    summa += int(arraysOfNumbers[i])
    i += 1
print(summa)

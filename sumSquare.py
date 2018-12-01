#!/usr/bin/python3

summa = 0;
sumSquare = 0;
while True:
    a = int(input())
    summa += a
    sumSquare = sumSquare + (a * a)
    if summa == 0:
        print(sumSquare)
        break

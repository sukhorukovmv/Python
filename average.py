#!/usr/bin/python3

a = int(input())
b = int(input())
quantityN = 0
s = 0
for a in range(a, b + 1, 1):
    if a % 3 == 0:
        quantityN = quantityN + 1
        s = s + a
print(s / quantityN)
        

#!/usr/bin/python3

a = int(input())
b = int(input())
if a > b:
    n = a
else:
    n = b
while (n % a != 0) or (n % b != 0):
    n = n + 1

print(n)

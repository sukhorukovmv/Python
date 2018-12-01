#!/usr/bin/python3

n = int(input())

if (n % 10 >= 1) and (n % 10 <= 4):
    if (n % 100 >= 11) and (n % 100 <= 14):
        print(n, "программистов")
    elif n % 10 == 1:
        print(n, "программист")
    else:
        print(n, "программиста")
else:
    print(n, "программистов")


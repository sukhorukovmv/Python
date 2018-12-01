#!/usr/bin/python3

a = int(input())
b = int(input())
c = int(input())
i = 1
while i < 10:
    if a >= b and a >= c:
        print(a)
        if b <= a and b <= c:
            print(b)
            print(c)
        else:
            print(c)
            print(b)
        break
    if b >= a and b >= c:
        print(b)
        if a <= b and a <= c:
            print(a)
            print(c)
        else:
            print(c)
            print(a)
        break
    else:
        print(c)
        if a <= b and a <= c:
            print(a)
            print(b)
        else:
            print(b)
            print(a)
        break

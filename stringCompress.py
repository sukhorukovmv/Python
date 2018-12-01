#!/usr/bin/python3

s = str(input())

result = ''
acc = 0
i = 0
symbol = s[0]
while i < len(s):
    if s[i] == symbol:
        acc = acc + 1
    else:
        result = result + symbol + str(acc)
        symbol = s[i]
        acc = 1
    i = i + 1
result = result + symbol + str(acc)

print(result)

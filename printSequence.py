#!/usr/bin/python3

n = int(input())
stringOut = ''
for i in range(1, n + 1, 1):
    stringOut += ((str(i) + ' ') * i)

print(*(stringOut.split(' '))[:n])
#stringOut = stringOut[:(n * 2)]
#print(stringOut)

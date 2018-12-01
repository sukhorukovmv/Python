#!/usr/bin/python3
import re
import math
lst = []
with open('dataset_3363_2.txt', 'r') as inf:
    lst = re.split('(\d*)',inf.readline().strip())

print(lst)
#print(stringIn)
stringOut = ''
print(len(lst))
for i in range(0, len(lst) - 1, 2):
    stringOut += (lst[i] * int(lst[i + 1]))

with open('output.txt', 'w') as out:
    out.write(stringOut)
print(stringOut)

r = int(input())
print(2 * pi * r)


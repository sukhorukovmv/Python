#!/usr/bin/python3

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print("\t", end = ' ')
j = c
for j in range(j, d + 1, 1):
    print(j, end = "\t")
print(end = '\n')

for a in range(a, b + 1, 1):
    print(a, end = '')
    j = c
    for j in range(j, d + 1, 1):
        print("\t", (j * a), end = '')
    print(end = '\n')
    
    
    

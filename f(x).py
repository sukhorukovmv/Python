#!/usr/bin/python3

def f(x):
    return x ** 2

n = int(input())
#lst = []
d = {}

for i in range(n):
    element = int(input())
    if element not in d:
        d.setdefault(element, f(element))
    print(d[element]) 
print(d)
#    lst.append(int(input()))
#print(lst)
#for element in lst:
#    print(d[element])
#print(d)
#print(d)
#d.setdefault(n, f(x))

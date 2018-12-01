#!/usr/bin/python3

string = str(input()).lower().split(' ')
d = {}
for word in string:
    d.setdefault(word, []).append(1)

for i in d:
    #print(d[i])
    #print(i.values())
    print(i, sum(d[i]))
    ##a = list(d.values())
    ##print(a)
##print(d)

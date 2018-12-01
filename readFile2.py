#!/usr/bin/python3
import re 
import math

#dct = {}
#with open('dataset_3363_3 (4).txt', 'r') as inf:
#    for line in inf:
#        line = inf.readline().lower().split()
#        for key in line:
#            dct.setdefault(key, []).append(1)


with open('input.txt', 'r') as text:
    lst = text.read().replace('\n', ' ').lower().split()
sortList = sorted(lst)
print(sortList)

#for x in sorted(lst):
    #print(x)

#opened = open('input.txt', 'r')
#lst = opened.read().replace('\n', ' ').lower().split()
#print(lst)
#opened.close()


#for i in dct:
#    print(i, sum(dct[i]))



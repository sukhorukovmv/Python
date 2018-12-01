#!/usr/bin/python

def modify_list(l):
    # put your python code here
    #n = len(l)
    #i = 0
    #while i < n:
    #    if l[i] % 2 == 0:
    #        l[i] = l[i] / 2;
    #        i += 1
    #    else:
    #        del l[i]
    #        n -= 1
    #for element in l[::-1]:
    #    if element % 2 == 0:
    #        element = element / 2
    #    else:
    #        l.remove(element)
    for i in range(len(l) - 1, 0 - 1, - 1):
        if l[i] % 2 == 0:
            l[i] = l[i] / 2
        else:
            del l[i]
            
#lst = [2, 2, 3]
#lst = [1, 2, 3, 4, 5, 6]
lst = [10, 5, 8, 3]
#lst = [0, 3, 5, 7, 9, 8]
#lst = [1, 1, 1, 1, 1, 1, 1]
print(lst)
modify_list(lst)
print(lst)

#!/usr/bin/python3

objects = [1, 2, 1, 2, 3]

if len(objects) == 0:
    print(0)
else:
    uniq = []
    uniq.append(objects[0])
    for i in objects:
        flag = True
        for j in uniq:
            if i is j:
                flag = False
        if flag:
            uniq.append(i)
    print(uniq)
    print(len(uniq))

#!/usr/bin/python3

with open("dataset_24465_4.txt") as original:
    array = [row.strip() for row in original]
with open('newFile.txt', 'w') as reverse:
    for line in reversed(array):
        reverse.write(line + '\n')
        #print(line)

    #with open('newFile.txt', 'a+') as reverse:
    #    print('newFile')
    #    reverse.writelines("second")

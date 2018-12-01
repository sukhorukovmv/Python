#!/usr/bin/python3

listNumbers = str(input()).split(' ')
numberSearch = int(input())
string = ''
for i in range(0, len(listNumbers), 1):
    if int(listNumbers[i]) == numberSearch:
        string += (str(i) + ' ')

if string == '':
    print("Отствует")
else:
    print(string)

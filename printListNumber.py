#!/usr/bin/python3

string = str(input())
lst = string.split(" ")
lst.sort()
string = ''
i = 0
while i < len(lst):
    if lst.count(lst[i]) > 1:
        string = string + str(lst[i]) + " "
    i += lst.count(lst[i]) 
print(string)
    
    

    


#!/usr/bin/python3

s = str(input()).lower()
print(len(s))
print(((s.count("c") + s.count("g")) / len(s)) * 100)

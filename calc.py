#!/usr/bin/python3

a = float(input())
b = float(input())
operation = str(input())
if operation == '+' :
    print(a + b)
if operation == '-' :
    print(a - b)
if operation == '/' :
    if b == 0 :
        print("Деление на 0!")
    else :
        print(a / b)
if operation == '*' :
    print(a * b)
if operation == 'mod' :
    if b == 0 :
        print("Деление на 0!")
    else :
        print(a % b)
if operation == 'pow' :
    print(a ** b)
if operation == 'div' :
    if b == 0 :
        print("Деление на 0!")
    else :
        print(a // b)
   
   


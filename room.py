#!/usr/bin/python3

import math

pi = 3.14
figure = str(input())
if figure == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2  
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)
if figure == 'прямоугольник':    
    a = float(input())
    b = float(input())
    print(a * b)
if figure == 'круг':
    a = float(input()) 
    print(pi * a ** 2)
   
   


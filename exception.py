#!/usr/bin/python3

try:
    foo()
except (ArithmeticError, AssertionError, ZeroDivisionError) as e: 
    print(type(e).__name__)

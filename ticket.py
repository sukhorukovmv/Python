#!/usr/bin/python3

ticket = str(input())

leftSum = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
rightSum = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if leftSum == rightSum:
    print("Счастливый")
else:
    print("Обычный")

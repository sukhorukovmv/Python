#!/usr/bin/python3

recommendedTime = int(input())
maximumSleep = int(input())
timeToSleep = int(input())

if timeToSleep >= recommendedTime and timeToSleep <= maximumSleep :
    print("Это нормально")
elif timeToSleep > maximumSleep :
    print("Пересып")
else :
    print("Heдосып")

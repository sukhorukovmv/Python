#!/usr/bin/python3

quantityOfMinutes = int(input())
beginSleepHour = int(input())
beginSleepMinute = int(input())

minutes = beginSleepMinute + quantityOfMinutes % 60
hours = quantityOfMinutes // 60
upMinutes = minutes % 60
upHours = beginSleepHour + hours + (minutes // 60)

print(upHours)
print(upMinutes)

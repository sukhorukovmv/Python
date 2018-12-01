#!/usr/bin/python3.6

class MoneyBox:
    def __init__(self, capasity):
        self.capasity = capasity
        self.level = 0

    def can_add(self, v):
        if self.level + v <= self.capasity:
            return True
        else:
            return False

    def add(self, v):
        self.level += v
        

mymoney = MoneyBox(100)
mymoney.add(50)
print(mymoney.level)
print(mymoney.can_add(50))
print(mymoney.level)


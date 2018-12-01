#!/usr/bin/python3.6

class Buffer:
    def __init__(self):
        self.list = []

    def add(self, *newList):
        quantityNumbers = 5
        for i in newList:
            self.list.append(i)

        lengthList = len(self.list) // 5

        for i in range(0, lengthList, 1):
            summa = 0
            for j in range(0, quantityNumbers, 1):
                summa += self.list[0]
                del self.list[0]
            print(summa)


    def get_current_part(self):
        print(self.list)

mylist = Buffer()
mylist.add(1, 2, 3)
mylist.get_current_part()
mylist.add(4, 5, 6)
mylist.get_current_part()
mylist.add(7, 8, 9, 10)
mylist.get_current_part()
mylist.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) 
mylist.get_current_part()

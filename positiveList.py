#!/usr/bin/python3
#class LoggableList(list, Loggable):
#    def append(self, x):
#        super(LoggableList, self).append(x)
#        self.log(x)

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError(x + "Not Positive")
        else:    
            super(PositiveList, self).append(x)
        

myPositiveList = PositiveList()
myPositiveList.append(4)
print(myPositiveList)
#myPositiveList.append(-4)
print(myPositiveList)


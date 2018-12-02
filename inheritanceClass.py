#!/usr/bin/python3

classDictionary = {}

def writeClassesInDictionary(d):
    n = int(input())###кол-во класов
    while len(classDictionary) != n:
        classAndChildren = str(input()).split()
        clas = classAndChildren[0]
        classDictionary.setdefault(clas, [])
        # if len(classDictionary) == n:
        #     break
        for child in classAndChildren[2:]:
            classDictionary.setdefault(child, [])
            classDictionary.setdefault(clas, []).append(child)
           # if len(classDictionary) == n: 
       #         break
def searchParent(d, parent, child):
    if not parent in d.keys() or not child in d.keys():
        return 'No'
    if child == parent:
        return 'Yes'
    if parent in d[child]:##если родитель есть в списке родителей child
        return 'Yes'
    ##если список родителей child пуст ретурн no 
    if d[child] == []:
        return 'No'
    else:
        answerString = ''##ответы со всех веток
        ###цикл проходит по всем веткам
        for newChild in d[child]:##передаем в searchParent нового child из списка родителей child
            answerString += (str(searchParent(d, parent, newChild)) + ' ')
        if 'Yes' in answerString.split():
            return 'Yes'
        else: 
            return 'No'

writeClassesInDictionary(classDictionary)
print(classDictionary)
for quantityRequests in range(0, int(input()), 1):
    parent, child = str(input()).split()
    #if parent in classDictionary[child]:
    #    print("Yes")
    #else:
    #    print("No")
    print(searchParent(classDictionary, parent, child))

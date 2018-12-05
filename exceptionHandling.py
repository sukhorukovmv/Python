#!/usr/bin/python3

def writeClassesInDictionary(d, n):
    if n == 0:
        return 0
    else:
        classAndChildren = str(input()).split()
        clas = classAndChildren[0]
        d.setdefault(clas, [])
        for child in classAndChildren[2:]:
            if clas != child:
                d.setdefault(child, [])
                d.setdefault(clas, []).append(child)
        return writeClassesInDictionary(d, n - 1)

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
            return 'Yes'#child
        else: 
            return 'No'

classDictionary = {}
writeClassesInDictionary(classDictionary, int(input()))

lstExcept = []
q = int(input())
lstExcept.append(str(input()))
for quantityExcept in range(1, q):
    currentExcept = str(input())
    for i in lstExcept:
        if searchParent(classDictionary, i, currentExcept) == 'Yes':
            print(currentExcept)
            break
    lstExcept.append(currentExcept)

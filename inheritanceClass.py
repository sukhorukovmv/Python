#!/usr/bin/python3

classDictionary = {}

list_to_input = ['A : B C D G H', 'B : C E G H K L', 'C : E D H K L', 'E : D F K L', 'D : G H', 'F : K', 'G : F', 'H : L', 'K : H L', 'L']

list_to_question=['K D', 'D A', 'G D', 'H A', 'E E', 'H G', 'E L', 'B D', 'D L', 'D G', 'D E', 'A F', 'A C', 'K A', 'A H', 'K D', 'H B', 'K B', 'D L', 'G G', 'A H', 'K L', 'G E', 'B A', 'C K', 'K L', 'C L', 'G C', 'D D', 'C G', 'E A', 'F K', 'B G', 'H L', 'L F', 'H G', 'D A', 'H L']#38 запросов

answers = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No']#38 ответов

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
            return 'Yes'
        else: 
            return 'No'

writeClassesInDictionary(classDictionary, int(input()))
print(classDictionary)
for quantityRequests in range(0, int(input()), 1):
    parent, child = str(input()).split()
    print(searchParent(classDictionary, parent, child))

""""
zapbezpiecznie  przez  krotke (tuple)- trotka nie  obsluguje zmiany  elementu 
evil_function(tuple(myList))

albo
evil_function(myList.copy()) - kopia plytka - opiuje cal liste


"""



def  evil_function(toBeDestroyedList):

    print(id(toBeDestroyedList))
    
   # toBeDestroyedList.clear()
    toBeDestroyedList[0] = 4

myList = [1, 4, 2, 1, 52, 3]

print(id(myList))
evil_function(myList.copy())
""""
albo
evil_function(list(myList))
evil_function(myList[:})


import copy

""""
deepcopy - glebokie kopiowanie

"""

def  evil_function(toBeDestroyedList):
    print(id(toBeDestroyedList))
    toBeDestroyedList[0][0] = 20
    print(toBeDestroyedList)

myList = [[1, 4], [2, 1], [52, 3]]

print(id(myList))
evil_function(copy.deepcopy(myList))



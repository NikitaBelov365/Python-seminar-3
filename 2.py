import random

def ListCreation(length):
    list1 = []
    for i in range(length):
        list1.append(random.randint(1, 10))
    print(list1)
    return list1

lst = ListCreation(5)

newList = lst[3:]
newList2 = lst[:3]

lastlist = newList+newList2
print(lastlist)
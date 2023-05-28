import random

def ListCreation(length):
    list1 = []
    for i in range(length):
        list1.append(random.randint(-10, 10))
    print(list1)
    return list1

def Solution(lst):
    newSet = set(lst)
    print(newSet)
    print(len(newSet))

listLength = int(input("Input list length: "))
Solution(ListCreation(listLength))

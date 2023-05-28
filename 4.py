import random

def ListCreation(length):
    list1 = []
    for i in range(length):
        list1.append(random.randint(-10, 10))
    print(list1)
    return list1

def Solution(list):
    counter = 0
    for i in range(1, len(list)):
        if list[i] > list[i-1]:
            counter += 1
            print(list[i], ">", list[i-1])
    return counter

length = int(input("Input length: "))
lst = ListCreation(length)
print(Solution(lst))
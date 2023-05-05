import random


# main
ArrayData = [[0] * 10 for x in range(0, 10)]
for x in range(10):
    for y in range(10):
        ArrayData[x][y] = random.randint(0, 100)


def OutputArray():
    global ArrayData
    for x in range(0, 10):
        for y in range(0, 10):
            print(ArrayData[x][y], "", end=" ")
        print()


# print("BEFORE")
# OutputArray()

# ArrayLength = 10
# for x in range(0, ArrayLength):
#     for y in range(0, ArrayLength - 1):
#         for z in range(0, ArrayLength - y - 1):
#             if ArrayData[x][z] > ArrayData[z][z + 1]:
#                 TempValue = ArrayData[x][z]
#                 ArrayData[x][z] = ArrayData[x][z + 1]
#                 ArrayData[x][z + 1] = TempValue

# print("AFTER")
OutputArray()


def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= 0:
        Mid = int((Lower + (Upper - 1)) / 2)
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1


search = int(input("Search: "))
index = BinarySearch(ArrayData, 0, 9, search)
print(index)

search = int(input("Search: "))
index = BinarySearch(ArrayData, 0, 9, search)
print(index)

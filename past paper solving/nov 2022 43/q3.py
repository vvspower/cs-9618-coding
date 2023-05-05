global ArrayNodes
ArrayNodes = [[-1] * 3 for x in range(0, 19)]

# for x in range(19):
#     for y in range(3):
#         print(ArrayNodes[x][y], " ", end=" ")
#     print()

ArrayNodes = [[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [
    1, 10, -1], [-1, 58, -1]]

FreeNode = 6
RootPointer = 0


def SearchValue(Root, ValueToFind):
    global ArrayNodes
    if Root == -1:
        return -1
    elif ArrayNodes[Root][1] == ValueToFind:
        return Root
    elif ArrayNodes[Root][1] == -1:
        return -1
    if (ArrayNodes[Root][1] > ValueToFind):
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if (ArrayNodes[Root][1] < ValueToFind):
        return SearchValue(ArrayNodes[Root][2], ValueToFind)


def PostOrder(RootNode):
    if RootNode[0] != -1:
        PostOrder(ArrayNodes[RootNode[0]])
    elif RootNode[2] != -1:
        PostOrder(ArrayNodes[RootNode[0]])
    print(str(RootNode[1]))

# main


Index = SearchValue(RootPointer, 15)
if Index != -1:
    print("Index of value found at is " + str(Index))
else:
    print("Value not found")
PostOrder(ArrayNodes[RootPointer])

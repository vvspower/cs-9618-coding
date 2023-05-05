global StackPointer  # integer
global StackData

StackPointer = 0
StackData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def OutputStack():
    print('OUTPUT STACK')
    print(StackPointer)
    for index in range(0, 10):
        print(StackData[index])


def Push(item):
    global StackPointer
    global StackData
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = item
        StackPointer = StackPointer + 1
        return True


def Pop():
    global StackPointer
    global StackData

    if StackPointer == 0:
        return -1
    else:
        Popped_Item = StackData[StackPointer - 1]
        StackPointer = StackPointer - 1
        return Popped_Item


# main
for x in range(0, 11):
    item = int(input("Enter Number: "))
    if Push(item):
        print("Item added Succesfully")
    else:
        print("Stack is full")
OutputStack()

Pop()
Pop()
OutputStack()

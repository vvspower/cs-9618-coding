global HeadPointer  # integer
global TailPointer  # integer
global NumberOfItems  # integer
global QueueArray

HeadPointer = 0
TailPointer = 0
NumberOfItems = 0
QueueArray = ["", "", "", "", "", "", "", "", "", ""]


def Enqueue(QueueArray, HeadPointer, TailPointer, NumberItems, DataToAdd):
    if NumberItems >= 10:
        return (False, QueueArray, HeadPointer, TailPointer, NumberItems)
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1
    NumberItems = NumberItems + 1
    return (True, QueueArray, HeadPointer, TailPointer, NumberItems)


def Dequeue(QueueArray, HeadPointer, TailPointer, NumberItems):
    if NumberOfItems == 0:
        return (False,  QueueArray, HeadPointer, TailPointer, NumberItems)
    else:
        Data = QueueArray[HeadPointer]
        HeadPointer = HeadPointer + 1
        if HeadPointer >= 9:
            HeadPointer = 0
        NumberItems = NumberItems - 1
        return (Data,   QueueArray, HeadPointer, TailPointer, NumberItems)


#  main

for x in range(0, 11):
    Value = str(input("Input Your Value: "))
    CheckEnqueue, QueueArray, HeadPointer, TailPointer, NumberOfItems = Enqueue(
        QueueArray, HeadPointer, TailPointer, NumberOfItems, Value)
    if CheckEnqueue:
        print("Successfully Added")
    else:
        print("Queue Full")
    print(QueueArray)


CheckDequeue, QueueArray, HeadPointer, TailPointer, NumberOfItems = Dequeue(
    QueueArray, HeadPointer, TailPointer, NumberOfItems)
print(CheckDequeue)
CheckDequeue, QueueArray, HeadPointer, TailPointer, NumberOfItems = Dequeue(
    QueueArray, HeadPointer, TailPointer, NumberOfItems)
print(CheckDequeue)

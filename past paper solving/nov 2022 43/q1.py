global DataArray
DataArray = [0 for x in range(0, 100)]


def ReadFile():
    try:
        File = open("IntegerData.txt", 'r')
        for x in range(0, 100):
            Number = int(File.readline())
            DataArray[x] = Number
    except IOError:
        print("File not found")


def FindValues():
    AppearsNum = 0
    NumberToSearch = -1
    while NumberToSearch == -1 and NumberToSearch < 1 or NumberToSearch > 100:
        NumberToSearch = int(input("Enter search value: "))
    for x in range(0, 100):
        if DataArray[x] == NumberToSearch:
            AppearsNum = AppearsNum + 1
    return AppearsNum


ReadFile()
AppearsNum = FindValues()
print("Value appears " + str(AppearsNum) + " times.")


def BubbleSort():
    global DataArray
    for x in range(0, 99):
        for y in range(0, 99):
            if DataArray[y] > DataArray[y + 1]:
                Temp = DataArray[y]
                DataArray[y] = DataArray[y + 1]
                DataArray[y + 1] = Temp
    print(DataArray)


BubbleSort()

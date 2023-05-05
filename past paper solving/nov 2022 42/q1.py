global NumberOfJobs
global Jobs

Jobs = [[0] * 2 for x in range(0, 100)]  # 2 by 100 array


def PrintArray():
    for x in range(0, NumberOfJobs):
        print(Jobs[x][0], "priority", Jobs[x][1])
    print()


def Initialize():
    global Jobs
    global NumberOfJobs

    for x in range(0, 100):
        for y in range(0, 2):
            Jobs[x][y] = -1

    NumberOfJobs = 0


def AddJob(JobNumber, Priority):
    global Jobs
    global NumberOfJobs

    for x in range(0, 100):
        if NumberOfJobs == 100:
            print("Not Added")
        if Jobs[x][0] == -1:
            Jobs[x][0] = JobNumber
            Jobs[x][1] = Priority
            NumberOfJobs = NumberOfJobs + 1
            print("Added")
            break


def InsertionSort():
    global Jobs
    global NumberOfJobs

    for i in range(1, NumberOfJobs):
        Current1 = Jobs[i][0]
        Current2 = Jobs[i][1]

        while i > 0 and Jobs[i - 1][1] > Current2:
            Jobs[i][0] = Jobs[i - 1][0]
            Jobs[i][1] = Jobs[i - 1][1]
            i = i - 1
        Jobs[i][0] = Current1
        Jobs[i][1] = Current2


Initialize()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)
InsertionSort()
PrintArray()

array = [13,1,5,2,34,56,8,9]
max_index = 8
n = max_index - 1

for i in range(0, max_index - 1):
    for j in range(0, n):
        if array[j] > array[j + 1]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp
    n = n - 1

print(array)
            
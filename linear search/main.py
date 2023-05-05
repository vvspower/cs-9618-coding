
#  linear search

list = [1,2,3,4,5,6,7,8,10]
search_item = 10

for x in range(len(list)):
    if list[x] == search_item:
        print("found")
        break
    

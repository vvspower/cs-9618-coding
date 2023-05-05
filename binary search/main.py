#  binary search

numbers = [4,8,15,20,47,60,65,74,85,90]
upper_bound = 9
lower_bound = 0
value_found = False
not_in_list = False

search_item = 60

while value_found == False and not_in_list == False :
    mid_point = int(( lower_bound + upper_bound ) / 2)
    if numbers[mid_point] == search_item:
        value_found = True
    elif numbers[mid_point] < search_item:
        lower_bound = mid_point + 1
    else:
        upper_bound = mid_point - 1
    if lower_bound > upper_bound:
        not_in_list = True
    


if value_found:
    print("present")
else:
    print("not found")
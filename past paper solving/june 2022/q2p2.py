def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper > Lower:
        Mid = (Lower + (Upper - 1)) % 2
        if SearchArray[0][Mid] == int(SearchValue):
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return - 1


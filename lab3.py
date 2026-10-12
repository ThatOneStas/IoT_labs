def bbl_sort(num_list):
    for i in range(len(num_list)):
        for j in range(0, len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list

def my_sum(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

def meanVsMedian(num_list):
    '''
    Accepts a list of numbers and returns a string indicating whether
    the mean or median is greater,or if they are the same.
    Raises an exception for even-length lists.
    '''
    result = ""
    if len(num_list) % 2 == 0:
        raise Exception("Only odd-length sequences are allowed")
    median = bbl_sort(num_list)[len(num_list) // 2]
    mean = my_sum(num_list) / len(num_list)
    if(median > mean):
        result = "median"
    elif (median < mean):
        result = "mean"
    else:
        result = "same"
    return result

try:
    print(meanVsMedian([1, 2, 3, 4, 5])) # same
    print(meanVsMedian([1, 10, 3, 4, 5])) # mean
    print(meanVsMedian([1, 2, 3, 5, 5, 6, 7])) # median
    print(meanVsMedian([1, 2, 3, 4, 5, 6])) # exception
    print(meanVsMedian([100, 2, 3, 4, 5, 6])) # will not be executed due to upper exception
except Exception as e:
    print(e)
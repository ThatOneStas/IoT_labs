def meanVsMedian(num_list):
    # нижче додав summary, аби не юзати коментарі
    '''
    Приймає лише непарні послідовності чисел.
    Повертає "median", якщо медіана більша за середнє, "mean", якщо середнє більше за медіану, або "same", якщо вони однакові.
    Якщо передана парна послідовність чисел, повертає виключення.
    '''
    if len(num_list) % 2 == 0:
        raise Exception("Лише непарні послідовності чисел")
    median = sorted(num_list)[len(num_list) // 2]
    mean = sum(num_list) / len(num_list)
    # print(median, mean)
    if(median > mean):
        return "median"
    elif (median < mean):
        return "mean"
    return "same"

try:
    print(meanVsMedian([1, 2, 3, 4, 5])) # same
    print(meanVsMedian([1, 10, 3, 4, 5])) # mean
    print(meanVsMedian([1, 2, 3, 5, 5, 6, 7])) # median
    print(meanVsMedian([1, 2, 3, 4, 5, 6])) # exception
    # тут обірветься, так як блок спіймав помилку з попереднього рядку
    print(meanVsMedian([100, 2, 3, 4, 5, 6]))
except Exception as e:
    print(e)
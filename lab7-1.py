def f(a, x):
    return a > x


# 1-1. Insertion sort
def insertion_sort(num_list: list[int]):
    list_len = len(num_list)

    for i in range(1, list_len):
        x = num_list[i]
        j = i - 1
        
        while j >= 0 and f(num_list[j], x):
            num_list[j + 1] = num_list[j]
            j -= 1
            
        num_list[j + 1] = x

    return num_list

print(insertion_sort([2, 1, 5, 7, 2, -22, 13, 0, -4, 33]))


# 1-2. Selection sort
def selection_sort(num_list: list[int]):
    list_len = len(num_list)

    for i in range(list_len):
        k = i
        for j in range(i + 1, list_len):
            if f(num_list[j], num_list[k]):
                k = j
        num_list[i], num_list[k] = num_list[k], num_list[i]
    
    return num_list

print(selection_sort([2, 1, 5, 7, 2, -22, 13, 0, -4, 33]))

# 1-3. Bubble sort
def bubble_sort(num_list: list[int]):
    list_len = len(num_list)
    for i in range(list_len):
        for j in range(list_len-1, i, -1):
            if f(num_list[j], num_list[j-1]):
                num_list[j-1], num_list[j] = num_list[j], num_list[j-1]

    return num_list

# def bubble_sort(num_list: list):
#     list_len = len(num_list)
#     for i in range(list_len):
#         for j in range(i+1, list_len):
#             if f(num_list[i], num_list[j]):
#                 num_list[i], num_list[j] = num_list[j], num_list[i]

#     return num_list

print(bubble_sort([2, 1, 5, 7, 2, -22, 13, 0, -4, 33]))
print()

# 2. Matrix
matrix = [
    [34,  45, 65,  23,  98],
    [1,   -4,  67,  -3, -18],
    [23,  -5,  -1,   94, -25],
    [2,  24, -4,   79, -63],
    [10,  29, 25,  30,  -6],
]

def fm(matrix: list[list[int]]):
    result = []
    outter_len = len(matrix)
    inner_len = len(matrix[0])
    for i in range(outter_len):
        a = 1
        b = 0
        for j in range(inner_len):
            if i < j:
                a *= matrix[i][j]
                b += 1
        if b != 0:
            result.append(round(pow(abs(a), 1/b), 3))
        else:
            result.append(0)
                    
    return result

def Fm(matrix: list[list[int]]):
    return sum(fm(matrix))

# def matrix_sort(matrix: list[list[int]]):
#     outter_len = len(matrix)
#     inner_len = len(matrix[0])
#     for i in range(inner_len):
#         for j in range(outter_len - 1):
#             for j in range(outter_len - 1):
#                 if matrix[j][i] > matrix[j+1][i]:
#                     matrix[j][i], matrix[j+1][i] = matrix[j+1][i], matrix[j][i]
#     return matrix

def matrix_sort(matrix: list[list[int]]):
    outter_len = len(matrix)
    inner_len = len(matrix[0])
    for i in range(inner_len):
        column = [matrix[j][i] for j in range(outter_len)]

        column = insertion_sort(column)

        for j in range(outter_len):
            matrix[j][i] = column[j]
    return matrix

matrix_sort(matrix)
for i in range(len(matrix)):
    print(matrix[i])

print(fm(matrix))
print(Fm(matrix))
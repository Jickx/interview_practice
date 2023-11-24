def zero_count(matrix):
    """ i - строка, j - столбец """
    i, j = 0, len(matrix) - 1
    result = 0
    iter_count = 0
    while i < len(matrix) and j >= 0:
        iter_count += 1
        if matrix[i][j] != 0:
            j -= 1
            continue
        result += j + 1
        i += 1
    return result, iter_count


matrix1 = [[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]]

matrix2 = [[0, 0, 0, 0, 1, 1, 1],
           [0, 0, 0, 1, 1, 1, 1],
           [0, 0, 0, 1, 1, 1, 1],
           [0, 0, 1, 1, 1, 1, 1],
           [0, 0, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1]]

print(zero_count(matrix1))

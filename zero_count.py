def zero_count(matrix):
    length = len(matrix)
    ctr = 0
    iter_ctr = 0
    for i in range(length):
        for j in range(length):
            iter_ctr += 1
            if matrix[i][j] != 0:
                break
            ctr += 1
    return ctr, iter_ctr


matrix = [[0, 0, 0, 0, 1, 1, 1],
          [0, 0, 0, 1, 1, 1, 1],
          [0, 0, 0, 1, 1, 1, 1],
          [0, 0, 1, 1, 1, 1, 1],
          [0, 0, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1]]

print(zero_count(matrix))

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
result1 = get_matrix(2, 4, 6)
result2 = get_matrix(3, 5, 7)
result3 = get_matrix(1, 3, 9)

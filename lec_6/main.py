import random

def generate_random__matrix(rows, cols):
    matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
    print('matrix generated`')
    [print(row) for row in matrix]
    return matrix

def get_column_sum(matrix, col_index):
    column_sum = sum(row[col_index] for row in matrix)
    print(f'get {col_index} column sum` ',column_sum)

def get_row_average(matrix, row_index):
    row_mean = round(sum(matrix[row_index])/len(matrix[row_index]), 3)
    print(f'get {row_index} row average` ',row_mean)

matrix = generate_random__matrix(4, 5)
get_column_sum(matrix, 2)
get_row_average(matrix, 2)
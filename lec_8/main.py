class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.columns = m
        self.matrix = [[0 for _ in range(m)] for _ in range(n)]

    def fill_matrix(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] = int(input(f"Enter element at position ({i+1}, {j+1}): "))

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        total_sum = sum(sum(row) for row in self.matrix)
        mean = total_sum / (self.rows * self.columns)
        return mean

    def calculate_row_sum(self, row_num):
        if 1 <= row_num <= self.rows:
            return sum(self.matrix[row_num - 1])
        else:
            return "Invalid row number"

    def calculate_column_average(self, col_num):
        if 1 <= col_num <= self.columns:
            col_sum = sum(row[col_num - 1] for row in self.matrix)
            col_avg = col_sum / self.rows
            return col_avg
        else:
            return "Invalid column number"

    def print_submatrix(self, col1, col2, row1, row2):
        if 1 <= col1 <= col2 <= self.columns and 1 <= row1 <= row2 <= self.rows:
            submatrix = [[self.matrix[i][j] for j in range(col1 - 1, col2)] for i in range(row1 - 1, row2)]
            for row in submatrix:
                print(row)
        else:
            print("Invalid submatrix coordinates")


# Example usage
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
matrix = Matrix(n, m)
matrix.fill_matrix()

print("Matrix:")
matrix.print_matrix()

print("Mean of the matrix:", matrix.calculate_mean())

row_num = int(input("Enter the row number to calculate sum: "))
print("Sum of row:", matrix.calculate_row_sum(row_num))

col_num = int(input("Enter the column number to calculate average: "))
print("Average of column:", matrix.calculate_column_average(col_num))

col1, col2, row1, row2 = map(int, input("Enter [col1, col2, row1, row2]: ").split())
print("Submatrix:")
matrix.print_submatrix(col1, col2, row1, row2)

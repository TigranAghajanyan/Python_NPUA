class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join(str(element) for element in row) + "\n"
        return matrix_str

    def fill_random(self):
        import random
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] = random.randint(1, 10)  # Fills matrix with random integers (1 to 10)

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result
        else:
            raise ValueError("Matrices must have the same dimensions for addition.")

    def __sub__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return result
        else:
            raise ValueError("Matrices must have the same dimensions for subtraction.")

    def __mul__(self, other):
        if self.columns == other.rows:
            result = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return result
        else:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")


# Example usage
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix1 = Matrix(rows, columns)
matrix1.fill_random()

matrix2 = Matrix(rows, columns)
matrix2.fill_random()

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

# Addition
try:
    result_addition = matrix1 + matrix2
    print("Addition Result:")
    print(result_addition)
except ValueError as e:
    print(e)

# Subtraction
try:
    result_subtraction = matrix1 - matrix2
    print("Subtraction Result:")
    print(result_subtraction)
except ValueError as e:
    print(e)

# Multiplication
try:
    result_multiplication = matrix1 * matrix2
    print("Multiplication Result:")
    print(result_multiplication)
except ValueError as e:
    print(e)

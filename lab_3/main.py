class VectorMatrixProduct:
    def __init__(self, vector, matrix, output_file):
        self.vector = vector
        self.matrix = matrix
        self.output_file = output_file

    def calculate_product(self):
        result = []
        for row in self.matrix:
            row_result = sum(a * b for a, b in zip(self.vector, row))
            result.append(row_result)
        return result

    def write_to_file(self, product):
        with open(self.output_file, 'w') as file:
            file.write(f"Vector: \n{self.vector}\n")
            file.write("\nMatrix:\n")
            for row in self.matrix:
                file.write("{}\n".format(row))
            file.write("\nProduct:\n")
            file.write("[{}]".format(', '.join(str(res) for res in product)))


        print(f"The result has been written to`  '{self.output_file}'.")

# Example usage
vector = [2, 3]
matrix = [
    [1, 2],
    [3, 4]
]
output_file = "lab_3/vector_matrix_product.txt"

# Create an instance of the class and perform calculations
calculator = VectorMatrixProduct(vector, matrix, output_file)
product_result = calculator.calculate_product()
calculator.write_to_file(product_result)

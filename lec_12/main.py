import random
import time

def generate_random_numbers():
    with open("lec_12/random_numbers_file.txt", "w") as file:
        for _ in range(100):
            numbers = [str(random.randint(-150, 150)) for _ in range(20)]
            file.write(" ".join(numbers) + "\n")

def calculate_the_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {function.__name__}: {end_time - start_time} \n")
        return result
    return wrapper

@calculate_the_time
def process_numbers():
    with open("lec_12/random_numbers_file.txt", "r") as file:
        lines = file.readlines()
        lines_numbers = map(lambda line: list(map(int, line.split())), lines)
        filtered_numbers = [list(filter(lambda number: number > 40, line_numbers)) for line_numbers in lines_numbers]

    with open("lec_12/my_filtered_numbers.txt", "w") as file:
        for arr in filtered_numbers:
            file.write(" ".join(map(str, arr)) + "\n")

@calculate_the_time
def read_filtered_file():
    with open("lec_12/my_filtered_numbers.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            yield list(map(int, line.split()))


generate_random_numbers()
process_numbers()

generator = read_filtered_file()


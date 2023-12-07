import random
import string
import time
import concurrent.futures
import multiprocessing

def generate_large_text_file(filename, num_words, word_length):
    with open(filename, 'w') as file:
        for _ in range(num_words):
            word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
            file.write(word + ' ')

def count_words(filename):
    word_freq = {}
    with open(filename, 'r') as file:
        words = file.read().split()
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq

def multithreaded_word_count(filename, num_threads):
    word_freq = {}
    with open(filename, 'r') as file:
        text = file.read()
        chunk_size = len(text) // num_threads
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    def count_words_in_chunk(chunk):
        nonlocal word_freq
        words = chunk.split()
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(count_words_in_chunk, chunks)

    return word_freq

def multiprocessing_word_count(filename, num_processes):
    word_freq = multiprocessing.Manager().dict()
    with open(filename, 'r') as file:
        text = file.read()
        chunk_size = len(text) // num_processes
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    def count_words_in_chunk(chunk, word_freq):
        words = chunk.split()
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    processes = []
    for i in range(num_processes):
        p = multiprocessing.Process(target=count_words_in_chunk, args=(chunks[i], word_freq))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return word_freq

# Main code
if __name__ == "__main__":
    file_name = 'large_text_file.txt'
    num_words = 100000 
    word_length = 5  

    generate_large_text_file(file_name, num_words, word_length)

    start_time = time.time()
    sequential_word_freq = count_words(file_name)
    sequential_time = time.time() - start_time

    start_time = time.time()
    multithreaded_word_freq = multithreaded_word_count(file_name, num_threads=4)
    multithreaded_time = time.time() - start_time

    start_time = time.time()
    multiprocessing_word_freq = multiprocessing_word_count(file_name, num_processes=4)
    multiprocessing_time = time.time() - start_time

    # Display results
    print("Sequential execution time:", sequential_time)
    print("Multithreaded execution time:", multithreaded_time)
    print("Multiprocessing execution time:", multiprocessing_time)

    multithreaded_speedup = round(sequential_time / multithreaded_time, 3)
    multiprocessing_speedup = round(sequential_time / multiprocessing_time, 3)

    print("Multithreaded speedup:", multithreaded_speedup)
    print("Multiprocessing speedup:", multiprocessing_speedup)

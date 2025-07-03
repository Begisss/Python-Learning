import threading
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def check_primes(start, end, result_list):
    for num in range(start, end):
        if is_prime(num):
            result_list.append(num)
def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    prime_results = []
    result_lock = threading.Lock()
    step = (end - start) // num_threads
    for i in range(num_threads):
        range_start = start + i * step
        range_end = start + (i + 1) * step if i < num_threads - 1 else end
        def thread_worker(s=range_start, e=range_end):
            temp_list = []
            check_primes(s, e, temp_list)
            with result_lock:
                prime_results.extend(temp_list)
        t = threading.Thread(target=thread_worker)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    prime_results.sort()
    return prime_results
if __name__ == "__main__":
    start_range = 1
    end_range = 100
    threads = 4

    primes = threaded_prime_checker(start_range, end_range, threads)
    print(f"Prime numbers between {start_range} and {end_range}:\n{primes}")

import threading
from collections import Counter
import os

def count_words(lines, result_list, index):
    word_count = Counter()
    for line in lines:
        words = line.strip().lower().split()
        word_count.update(words)
    result_list[index] = word_count

def threaded_word_count(filename, num_threads=4):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    results = [None] * num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        thread = threading.Thread(target=count_words, args=(lines[start:end], results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_count = Counter()
    for wc in results:
        total_count.update(wc)

    print("Top 10 most common words:")
    for word, count in total_count.most_common(10):
        print(f"{word}: {count}")

    return total_count

if __name__ == "__main__":
    if not os.path.exists("large_text.txt"):
        with open("large_text.txt", "w") as f:
            f.write("This is a sample line.\n" * 10000)  # Generate a dummy file

    threaded_word_count("large_text.txt", num_threads=4)


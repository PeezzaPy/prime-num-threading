import threading
import time

def is_prime_num(my_num):
    if my_num <= 1:
        return False
    if my_num <= 3:
        return True
    if my_num % 2 == 0:
        return False

    for divisor in range(3, int((my_num**0.5)+1), 2):
        if my_num % divisor == 0:
            return False
    return True


def find_prime_in_range(thread_num, start, end, output_prime_numbers):
    prime_numbers = []

    for num in range(start, end):
        if is_prime_num(num):
            prime_numbers.append(num)
            # To see the progress of multiprocessing
            print(f"Thread # {thread_num+1} : {num}")
            time.sleep(1)

    output_prime_numbers.extend(prime_numbers)
            
    # Without the progress
    # prime_numbers = [num for num in range(start, end) if is_prime_num(num)]
    # output_prime_numbers.extend(prime_numbers)


def main():
    threads = []
    output_prime_numbers = []
    num_of_threads = 4
    start_num = 1
    end_num = 1000
    chunk_size_per_thread = (end_num - start_num) // num_of_threads

    for i in range(num_of_threads):
        thread_start = start_num + i * chunk_size_per_thread
        thread_end = thread_start + chunk_size_per_thread
        thread = threading.Thread(target=find_prime_in_range, args=(i, thread_start, thread_end, output_prime_numbers))
        threads.append(thread)
        thread.start()

    # main thread waits for all the sub-thread
    for thread in threads:
        thread.join()


    print("\n\nArray of prime numbers:\n", sorted(output_prime_numbers))



if __name__ == "__main__":
    main()
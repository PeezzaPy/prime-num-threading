import threading
import time


def is_prime_num(my_num):
    if my_num <= 1:
        return False
    if my_num <= 3:
        return True
    if my_num % 2 == 0:
        return False

    for divisor in range(3, int((my_num ** 0.5) + 1), 2):
        if my_num % divisor == 0:
            return False
    return True


def find_prime_in_range(start, end, output_prime_numbers):
    prime_numbers = []

    for num in range(start, end):
        if is_prime_num(num):
            prime_numbers.append(num)
            # using delay to see the progress of multiprocessing
            print(f"\nThread # {thread_num+1} : {num}")
            #time.sleep(1)

    output_prime_numbers.extend(prime_numbers)

    # Without the progress
    # prime_numbers = [num for num in range(start, end) if is_prime_num(num)]
    # output_prime_numbers.extend(prime_numbers)


def main():
    threads, thread_start, thread_end = [], [], []
    output_prime_numbers = []

    # Get input from the user
    print("=-=-= PRIME NUMBER CALCULATOR USING MULTI-THREADING =-=-=", end="\n\n")
    start_num = get_integer_input("Enter the start number: ")
    end_num = get_integer_input("Enter the end number: ")
    num_of_threads = get_integer_input("Enter number of threads: ")

    # calculate the size per thread
    chunk_size_per_thread = (end_num - start_num) // num_of_threads

    # MULTI-THREADING
    for i in range(num_of_threads):
        start = start_num + i * chunk_size_per_thread
        end = start + chunk_size_per_thread
        thread_start.append(start)
        thread_end.append(end)

    start_time = time.time()     
    for i in range(num_of_threads):
        thread = threading.Thread(target=find_prime_in_range, args=(thread_start[i], thread_end[i], output_prime_numbers))
        threads.append(thread)
        thread.start()
    end_time = time.time() 
    execution_time = end_time - start_time

    # main thread waits for all the sub-thread
    for thread in threads:
        thread.join()


    print("\n\nArray of prime numbers:\n", sorted(output_prime_numbers))



if __name__ == "__main__":
    main()

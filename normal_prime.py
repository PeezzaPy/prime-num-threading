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


def find_prime_in_range(start, end, output_prime_numbers):
    prime_numbers = []

    for num in range(start, end):
        if is_prime_num(num):
            prime_numbers.append(num)
    output_prime_numbers.extend(prime_numbers)


def main():
    output_prime_numbers = []
    start_num = 1
    end_num = 100000

    start_time = time.time()        # start time record
    find_prime_in_range(start_num, end_num, output_prime_numbers)
    end_time = time.time()          # end time record
    execution_time = end_time - start_time

    print("\n\nArray of prime numbers:\n", sorted(output_prime_numbers), end="\n\n")
    print(f"Execution time: {execution_time} seconds")


if __name__ == "__main__":
    main()
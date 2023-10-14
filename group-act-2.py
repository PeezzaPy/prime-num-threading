from tkinter import font as tkFont
from tkinter import Scrollbar
import tkinter as tk
import threading
import time

output_prime_numbers = []

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


def find_prime_in_range(thread_num, start, end):
    prime_numbers = []

    for num in range(start, end):
        if is_prime_num(num):
            prime_numbers.append(num)
            print(f"\nThread # {thread_num+1} : {num}")
            # using delay to see the progress of multiprocessing
            # time.sleep(1)

    output_prime_numbers.extend(prime_numbers)
    # Without the progress
    # prime_numbers = [num for num in range(start, end) if is_prime_num(num)]
    # output_prime_numbers.extend(prime_numbers)

def update_display():
    display_text.delete(1.0, tk.END)
    display_text.insert(tk.END, ", ".join(map(str, sorted(output_prime_numbers))))

def calculating_prime_number():
    threads = []
    num_of_threads = 3
    start_num = 1
    end_num = 200
    chunk_size_per_thread = (end_num - start_num) // num_of_threads

    for i in range(num_of_threads):
        thread_start = start_num + i * chunk_size_per_thread
        thread_end = thread_start + chunk_size_per_thread
        thread = threading.Thread(target=find_prime_in_range, args=(i, thread_start, thread_end))
        threads.append(thread)
        thread.start()

    # main thread waits for all the sub-thread
    for thread in threads:
        thread.join()

    root.after(1000, update_display)



# Create a window
root = tk.Tk()
root.title("Prime Number Calculator using Multi-threading")
root.geometry("800x400")
custom_font = tkFont.Font(family="Helvetica", size=14, weight="bold")

# Create a frame to contain the display text
frame = tk.Frame(root)
frame.pack(side="left")

output_prime_numbers_var = tk.StringVar()

calculate_button = tk.Button(root, text="Calculate Prime Numbers", font=custom_font, command=calculating_prime_number)
calculate_button.pack(side="bottom", pady=20)

display_label = tk.Label(root, text="Array of\nprime numbers:", font=custom_font)
display_label.pack(side="left", anchor="n", padx=20,pady=20)

display_text = tk.Text(root, font=custom_font, wrap="none")
display_text.pack(fill="both", expand=True)

# Create a scrollbar
scrollbar = Scrollbar(root, orient="vertical", command=display_text.yview)
scrollbar.pack(side="right", fill="y")

display_text.config(yscrollcommand=scrollbar.set)

root.mainloop()

    



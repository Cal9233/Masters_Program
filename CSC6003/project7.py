import random
import time

# Function to generate a list of random numbers
def generate_random_list(size, lower_bound=0, upper_bound=10000):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# Merge Sort Algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Shell Sort Algorithm
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Main function
if __name__ == "__main__":
    # Generate a list of random numbers
    size = 10000  # Adjust the size for larger data
    random_list = generate_random_list(size)

    # Time Merge Sort
    merge_list = random_list.copy()
    print("Starting Merge Sort...")
    start_time = time.time()
    merge_sort(merge_list)
    end_time = time.time()
    print(f"Merge Sort took {end_time - start_time:.6f} seconds")

    # Time Shell Sort
    shell_list = random_list.copy()
    print("Starting Shell Sort...")
    start_time = time.time()
    shell_sort(shell_list)
    end_time = time.time()
    print(f"Shell Sort took {end_time - start_time:.6f} seconds")
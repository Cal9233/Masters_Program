import random
import timeit

# Function to generate a list of random numbers
def generate_random_list(size, low=0, high=10000):
    return [random.randint(low, high) for _ in range(size)]

# Merge Sort Algorithm
def merge_sort_alg(arr):
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    width = 1
    n = len(arr)
    while width < n:
        for i in range(0, n, 2*width):
            arr[i:i+2*width] = merge(arr[i:i+width], arr[i+width:i+2*width])
        width *= 2
    return arr

# Shell Sort Algorithm
def shell_sort_alg(arr):
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
    return arr

# Main function
if __name__ == "__main__":
    # Generate a list of random numbers
    size = 10000
    random_list = generate_random_list(size)

    # Time Merge Sort
    merge_list = random_list.copy()
    print("Starting Merge Sort Algorithm...")
    merge_alg_execution_time = timeit.timeit(lambda: merge_sort_alg(merge_list.copy()), number=1)
    print(f"Merge Sort Algorithm took {merge_alg_execution_time:.6f} seconds")

    # Time Shell Sort
    shell_list = random_list.copy()
    print("Starting Shell Sort Algorithm...")
    shell_alg_execution_time = timeit.timeit(lambda: shell_sort_alg(shell_list.copy()), number=1)
    print(f"Shell Sort Algorithm took {shell_alg_execution_time:.6f} seconds")
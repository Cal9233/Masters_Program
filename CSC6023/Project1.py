import random
import cProfile

def quick_sort(arr):
    """
    Implement the quicksort algorithm to sort an array in ascending order.

    Args:
    :param arr (list): The input array to be sorted.

    Returns:
    list: The sorted array.
    """
    length = len(arr)
    if length <= 1:
        return arr
    else:
    # Choose the last element as the pivot
        pivot = arr.pop()
    #Subarrays containing elements greater or smaller than pivot
    items_greater = []
    items_lower = []
    # Partition the array
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    # Recursively sort the partitions and combine the result
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


def main():
    """
    Main function to generate test vectors, run quicksort, and profile its performance.
    """
    # Generate test vectors of different sizes
    vector_1k = [random.random() for _ in range(0, 1000)]
    vector_2k = [random.random() for _ in range(0, 2000)]
    vector_3k = [random.random() for _ in range(0, 3000)]
    vector_4k = [random.random() for _ in range(0, 4000)]
    vector_5k = [random.random() for _ in range(0, 5000)]
    vector_6k = [random.random() for _ in range(0, 6000)]
    vector_7k = [random.random() for _ in range(0, 7000)]
    vector_8k = [random.random() for _ in range(0, 8000)]
    vector_9k = [random.random() for _ in range(0, 9000)]
    vector_10k = [random.random() for _ in range(0, 10000)]
    # Combine all vectors into a list
    all_vectors = [vector_1k, vector_2k, vector_3k, vector_4k, vector_5k, vector_6k, vector_7k, vector_8k, vector_9k, vector_10k]
    # Initialize the profiler
    profiler = cProfile.Profile()
    # Profile quicksort for each vector
    for i, vector in enumerate(all_vectors, start=1):
        profiler.enable()
        quick_sort(vector)
        profiler.disable()
        print(f"Profiling result for vector_{i}:")
        profiler.print_stats()
        profiler.clear()

if __name__ == "__main__":
    main()
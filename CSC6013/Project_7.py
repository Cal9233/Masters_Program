import random

def QuickSelect(arr, k):
    """
    Finds the k-th smallest element in the given array using the QuickSelect algorithm.
    
    Args:
    arr (list): The input array to search.
    k (int): The position of the element to find (1-indexed).
    
    Returns:
    The k-th smallest element in the array.
    """
    def select_wrapper(arr, l, h, k):
        """
        Recursive helper function for QuickSelect.
        
        Args:
        arr (list): The input array or subarray.
        l (int): The left boundary of the current subarray.
        h (int): The right boundary of the current subarray.
        k (int): The position of the element to find within the current subarray.
        
        Returns:
        The k-th smallest element in the subarray.
        """
        if l == h:
            return arr[l]
        
        pivot_i = partition(arr, l, h)

        if k == pivot_i - l + 1:
            return arr[pivot_i]
        elif k < pivot_i - l + 1:
            return select_wrapper(arr, l, pivot_i - 1, k)
        else:
            return select_wrapper(arr, pivot_i + 1, h, k - (pivot_i - l + 1))
        
    return select_wrapper(arr, 0, len(arr) - 1, k)

def partition(arr, l, h):
    """
    Partitions the array around a pivot element.
    
    Args:
    arr (list): The array or subarray to partition.
    l (int): The left boundary of the subarray to partition.
    h (int): The right boundary of the subarray to partition.
    
    Returns:
    The index of the pivot element after partitioning.
    """
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def main():
    """
    Main function to demonstrate the QuickSelect algorithm.
    
    Generates a random list of 1000 integers, prompts the user for a value k,
    and finds the k-th smallest element using QuickSelect.
    """
    random_list = [random.randint(1, 1000) for _ in range(1000)]

    while True:
        try:
            k = int(input("Please enter a value for k (1 <= k <= 1000): "))
            if 1 <= k <= 1000:
                break
            else:
                print("Please enter a value between 1 and 1000.")
        except ValueError:
            print("Please enter a valid integer.")
        except (KeyboardInterrupt, EOFError):
            print("Closing program.")
            exit()
        
    result = QuickSelect(random_list, k)
    print(f"The {k}-th smallest element in the array is: {result}")

if __name__ == "__main__":
    main()
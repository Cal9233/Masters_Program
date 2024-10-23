def Partition(arr, left, right):
    """
    Partitions the array around a pivot element such that all elements
    smaller than or equal to the pivot are on the left, and all elements
    greater than the pivot are on the right.

    Parameters:
    arr (list): The array to be partitioned.
    left (int): The starting index of the portion of the array being partitioned.
    right (int): The ending index of the portion of the array being partitioned (the pivot).

    Returns:
    int: The index position of the pivot after partitioning.
    """
    pivot = arr[right]  # Choose the rightmost element as the pivot
    i = left  # Pointer for the smaller element

    # Loop through the array from 'left' to 'right - 1'
    for j in range(left, right):
        # If current element is smaller or equal to the pivot
        if arr[j] <= pivot:
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
            i += 1  # Move pointer for the smaller element
    
    # Swap the pivot element with the element at the partition index 'i'
    arr[i], arr[right] = arr[right], arr[i]
    
    # Return the partition index where the pivot is located
    return i

def QuickSort(arr, left, right):
    """
    Recursively sorts the array by partitioning it and sorting the left and right subarrays.

    Parameters:
    arr (list): The array to be sorted.
    left (int): The starting index of the portion of the array to sort.
    right (int): The ending index of the portion of the array to sort.

    Returns:
    None: The array is sorted in place.
    """
    # Base case: Only proceed if the left index is less than the right index
    if left < right:
        # Partition the array and get the pivot index
        mid = Partition(arr, left, right)
        
        # Recursively apply QuickSort to the left subarray
        QuickSort(arr, left, mid - 1)
        
        # Recursively apply QuickSort to the right subarray
        QuickSort(arr, mid + 1, right)

def main():
    """
    Main function that initializes an array, calls QuickSort, and prints the sorted array.
    """
    # Initialize the list of numbers
    arr = [99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    
    # Call QuickSort on the entire array
    QuickSort(arr, 0, len(arr) - 1)
    
    # Print the sorted array
    print(arr)

# Execute the main function
main()

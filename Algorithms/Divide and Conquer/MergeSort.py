def MergeSort(arr):
    """
    Recursively divides the input array into smaller subarrays until
    the base case is reached (an array of one or fewer elements), and then
    merges them back together in sorted order.

    Parameters:
    arr (list): The array to be sorted.

    Returns:
    list: A sorted version of the input array.
    """
    # Base case: if the array has one or fewer elements, it's already sorted.
    if len(arr) <= 1:
        return arr
    else:
        # Find the midpoint of the array to divide it into two halves
        mid_point = len(arr) // 2
        
        # Recursively apply MergeSort to the left and right halves
        left = MergeSort(arr[:mid_point])
        right = MergeSort(arr[mid_point:])
        
        # Merge the sorted halves
        return Merge(left, right)

def Merge(left, right):
    """
    Merges two sorted arrays (left and right) into one sorted array.

    Parameters:
    left (list): The left half of the array, which is already sorted.
    right (list): The right half of the array, which is already sorted.

    Returns:
    list: A single merged array, containing all elements from left and right in sorted order.
    """
    result = []  # Initialize the result array that will hold the merged elements
    i, j = 0, 0  # Initialize two pointers to traverse the left and right arrays

    # Loop until either left or right array is fully processed
    while i < len(left) and j < len(right):       
        # Compare the elements from both arrays and append the smaller one to the result
        if left[i] < right[j]:
            result.append(left[i])
            i += 1  # Move the pointer in the left array
        else:
            result.append(right[j])
            j += 1  # Move the pointer in the right array
    
    # If there are remaining elements in the left array, append them to the result
    result += left[i:]    
    # If there are remaining elements in the right array, append them to the result
    result += right[j:]
    
    return result

# Example usage:
array = [12, 5, 36, 78, 1, 54]
print(MergeSort(array))
def count_divisible(arr, divisor):
    """
    Count the number of entries in an array that are divisible by a given integer.
    
    Parameters:
    arr (list of int): The array of integers to check.
    divisor (int): The positive integer to divide by.
    
    Returns:
    int: The count of entries in the array that are divisible by the divisor.
    """
    count = 0
    for num in arr:
        if num % divisor == 0:
            count += 1
    return count

def smallest_gap(arr):
    """
    Find the smallest gap between all pairs of elements in an array.
    
    Parameters:
    arr (list of float): The array of real numbers.
    
    Returns:
    float: The smallest absolute difference between any two elements in the array.
    """
    min_gap = float('inf')  # Initialize to a large value
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            gap = abs(arr[i] - arr[j])
            if gap < min_gap:
                min_gap = gap
    return min_gap

def matrix_product(n, A, B):
    """
    Calculate the product of two nxn matrices.
    
    Parameters:
    n (int): The size of the matrices (n x n).
    A (list of list of float): The first matrix.
    B (list of list of float): The second matrix.
    
    Returns:
    list of list of float: The product matrix AB.
    """
    # Initialize the product matrix with zeros
    product = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                product[i][j] += A[i][k] * B[k][j]
    return product

if __name__ == "__main__":
    # Problem 1
    arr1 = [20, 21, 25, 28, 33, 34, 35, 36, 41, 42]
    divisor1 = 7
    result1 = count_divisible(arr1, divisor1)
    print(f"Number of entries in {arr1} divisible by {divisor1}: {result1}")

    arr2 = [18, 54, 76, 81, 36, 48, 99]
    divisor2 = 9
    result2 = count_divisible(arr2, divisor2)
    print(f"Number of entries in {arr2} divisible by {divisor2}: {result2}")

    # Problem 2
    arr3 = [50, 120, 250, 100, 20, 300, 200]
    result3 = smallest_gap(arr3)
    print(f"Smallest gap in {arr3}: {result3}")

    arr4 = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]
    result4 = smallest_gap(arr4)
    print(f"Smallest gap in {arr4}: {result4}")

    # Problem 3
    n1 = 2
    A1 = [[2, 7], [3, 5]]
    B1 = [[8, -4], [6, 6]]
    result5 = matrix_product(n1, A1, B1)
    print(f"Product of matrices A and B:\n{result5}")

    n2 = 3
    A2 = [[1, 0, 2], [3, -2, 5], [6, 2, -3]]
    B2 = [[0.3, 0.25, 0.1], [0.4, 0.8, 0], [-0.5, 0.75, 0.6]]
    result6 = matrix_product(n2, A2, B2)
    print(f"Product of matrices A and B:\n{result6}")



################################################################################
def count_divisible_entries(arr, divisor):
    """
    Count the number of entries in an array that are divisible by a given integer.
    
    Input:
    arr (list of int): The array of integers to check
    divisor (int): The positive integer to divide by
    
    Output:
    int: The count of entries divisible by the divisor
    """
    # Use a list comprehension to count divisible entries
    return sum(1 for num in arr if num % divisor == 0)

# Driver code
if __name__ == "__main__":
    # Test case a
    arr_a = [20, 21, 25, 28, 33, 34, 35, 36, 41, 42]
    divisor_a = 7
    print(f"a) Number of entries divisible by {divisor_a}: {count_divisible_entries(arr_a, divisor_a)}")

    # Test case b
    arr_b = [18, 54, 76, 81, 36, 48, 99]
    divisor_b = 9
    print(f"b) Number of entries divisible by {divisor_b}: {count_divisible_entries(arr_b, divisor_b)}")


    def find_smallest_gap(arr):
        """
        Find the smallest gap between all pairs of elements in an array of numbers.
        
        Input:
        arr (list of float): The array of numbers to check
        
        Output:
        float: The smallest gap between any pair of elements
        """
        # Initialize smallest_gap to positive infinity
        smallest_gap = float('inf')
        
        # Compare each element with every other element
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                # Calculate the absolute difference
                gap = abs(arr[i] - arr[j])
                # Update smallest_gap if this gap is smaller
                smallest_gap = min(smallest_gap, gap)
        
        return smallest_gap

# Driver code
if __name__ == "__main__":
    # Test case a
    arr_a = [50, 120, 250, 100, 20, 300, 200]
    print(f"a) Smallest gap: {find_smallest_gap(arr_a)}")

    # Test case b
    arr_b = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]
    print(f"b) Smallest gap: {find_smallest_gap(arr_b)}")


def matrix_multiply(n, A, B):
    """
    Multiply two nxn matrices A and B.
    
    Input:
    n (int): The size of the matrices (n x n)
    A (list of list of float): The first matrix
    B (list of list of float): The second matrix
    
    Output:
    list of list of float: The product matrix AB
    """
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    # Perform matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Helper function to print matrices nicely
def print_matrix(matrix):
    for row in matrix:
        print([round(x, 2) for x in row])

# Driver code
if __name__ == "__main__":
    # Test case a
    n_a = 2
    A_a = [[2, 7], [3, 5]]
    B_a = [[8, -4], [6, 6]]
    print("a) Result of matrix multiplication:")
    print_matrix(matrix_multiply(n_a, A_a, B_a))

    print()

    # Test case b
    n_b = 3
    A_b = [[1, 0, 2], [3, -2, 5], [6, 2, -3]]
    B_b = [[0.3, 0.25, 0.1], [0.4, 0.8, 0], [-0.5, 0.75, 0.6]]
    print("b) Result of matrix multiplication:")
    print_matrix(matrix_multiply(n_b, A_b, B_b))
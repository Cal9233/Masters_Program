import math
import random
import unittest

class TestHillClimb(unittest.TestCase):
    def test_parameter_acceptance(self):
        """Test that function accepts array and start_index parameters"""
        result = hillClimb([1, 2, 3], 0)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        
    def test_return_format(self):
        """Test that function returns index and value as separate values, not in a list"""
        index, value = hillClimb([1, 2, 1], 0)
        self.assertIsInstance(index, int)
        self.assertIsInstance(value, (int, float))
        
    def test_starting_index_is_peak(self):
        """Test when starting index is already a local peak"""
        test_cases = [
            ([1, 2, 1], 1),  # Simple peak
            ([1, 3, 3, 1], 1),  # Peak at start of shoulder
            ([1, 3, 3, 3, 1], 1),  # Peak at start of longer shoulder
        ]
        for arr, start in test_cases:
            index, value = hillClimb(arr, start)
            self.assertEqual(index, start)
            self.assertEqual(value, arr[start])
            
    def test_equal_increases_go_right(self):
        """Test that function chooses right path when increases are equal"""
        test_cases = [
            ([1, 0, 1], 1),  # Simple equal increases
            ([2, 0, 2, 3], 1),  # Equal initial increases, higher on right
            ([2, 0, 2, 1], 1),  # Equal initial increases, peak on right
        ]
        for arr, start in test_cases:
            index, _ = hillClimb(arr, start)
            self.assertGreater(index, start)
            
    def test_unequal_increases_follow_higher(self):
        """Test that function follows the higher increase path"""
        test_cases = [
            ([3, 0, 2], 1),  # Higher increase on left
            ([2, 0, 3], 1),  # Higher increase on right
            ([4, 1, 3, 2], 1),  # Multiple steps, higher left
        ]
        for arr, start in test_cases:
            index, value = hillClimb(arr, start)
            self.assertEqual(value, max(arr))
            
    def test_array_boundaries(self):
        """Test that function can reach array boundaries"""
        test_cases = [
            ([5, 4, 3, 2, 1], 4),  # Need to go left to boundary
            ([1, 2, 3, 4, 5], 0),  # Need to go right to boundary
            ([3, 2, 1, 2, 3], 2),  # Can go either direction to peak
        ]
        for arr, start in test_cases:
            index, value = hillClimb(arr, start)
            self.assertEqual(value, max(arr))
            
    def test_shoulder_traversal(self):
        """Test shoulder handling according to specifications"""
        test_cases = [
            # Should return index 0, value 6
            ([6, 5, 5, 5, 4, 3, 2], 5, 0, 6),
            # Should return index 1, value 5
            ([2, 5, 5, 5, 4, 3, 2], 5, 1, 5),
            # Complex shoulder cases
            ([1, 5, 5, 5, 5, 4], 2, 1, 5),
            ([4, 5, 5, 5, 5, 6], 2, 5, 6),
            ([3, 3, 3, 3], 1, 0, 3),  # All equal values
        ]
        for arr, start, expected_index, expected_value in test_cases:
            index, value = hillClimb(arr, start)
            self.assertEqual(index, expected_index)
            self.assertEqual(value, expected_value)
            
    def test_random_real_cases(self):
        """Test with random inputs using myFunction"""
        # Generate test array
        arr = [myFunction(x) for x in range(100)]
        
        # Test multiple random starting positions
        for _ in range(10):
            start = random.randint(0, len(arr) - 1)
            index, value = hillClimb(arr, start)
            
            # Verify we're at a local maximum
            if index > 0:
                self.assertGreaterEqual(value, arr[index - 1])
            if index < len(arr) - 1:
                self.assertGreaterEqual(value, arr[index + 1])

def log2(x):
    """
    Helper function that returns log of x.
    
    Args:
        x (int): Number to calculate log2 of.
        
    Returns:
        float: Result of log2(x).
    """
    return math.log2(x) if x > 0 else 0

def myFunction(x):
    """
    Test function to be optimized.
    
    Args:
        x (int): Input value
        
    Returns:
        float: Result of function calculation
    """
    if x == 0:
        return 0
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x)) ** 3
    elif ((log2(x) * 5) % 23) < (x % 19):
        return (log2(x) * 2) ** 3
    else:
        return (log2(x) ** 2) - x

def hillClimb(arr, start_index):
    """
    Implements hill climbing algorithm to find local maximum.
    
    Args:
        arr (list): Array of values
        start_index (int): Starting position for search
        
    Returns:
        tuple: (index of local maximum, value at that index)
    """
    current_index = start_index
    
    while True:
        left_better = False
        right_better = False
        left_value = float('-inf')
        right_value = float('-inf')
        
        # Check left neighbor if exists
        if current_index > 0:
            left_value = arr[current_index - 1]
            left_better = left_value > arr[current_index]
            
        # Check right neighbor if exists
        if current_index < len(arr) - 1:
            right_value = arr[current_index + 1]
            right_better = right_value > arr[current_index]
            
        # If current position is peak or shoulder
        if not left_better and not right_better:
            # First check for higher values to the left
            temp_index = current_index
            while temp_index > 0 and arr[temp_index - 1] >= arr[temp_index]:
                if arr[temp_index - 1] > arr[temp_index]:
                    temp_index -= 1
                    break
                temp_index -= 1
            
            if temp_index != current_index:
                current_index = temp_index
                continue
                
            # If no higher values to the left, check shoulder to the right
            temp_index = current_index
            while temp_index < len(arr) - 1 and arr[temp_index] == arr[temp_index + 1]:
                temp_index += 1
                
            # If shoulder ends with a higher value, move to it
            if temp_index < len(arr) - 1 and arr[temp_index + 1] > arr[temp_index]:
                current_index = temp_index + 1
                continue
                
            # We've found our peak
            return current_index, arr[current_index]

        # Handle equal increases (go right as specified)
        if left_better and right_better and left_value == right_value:
            current_index += 1
        # Handle unequal increases (go toward higher value)
        elif left_better and right_better:
            current_index = current_index - 1 if left_value > right_value else current_index + 1
        # Handle single direction increase
        elif left_better:
            current_index -= 1
        else:
            current_index += 1

def main():
    # Generate array using myFunction
    arr = [myFunction(x) for x in range(10000)]

    # Set high number of attempts for Monte Carlo style
    num_attempts = 5000
    best_local_max = float('-inf')
    global_max = max(arr)
    
    # Run hill climbing multiple times with attempts for Monte Carlo style
    for _ in range(num_attempts):
        start_index = random.randint(1, 9998)
        _, local_max = hillClimb(arr, start_index)
        best_local_max = max(best_local_max, local_max)
    
    # Print results
    if best_local_max == global_max:
        print(f"After {num_attempts} tries, the greatest local maximum discovered was {best_local_max} which was the global maximum.")
    # Update num_attempts to smaller value like 50 to hit else condition
    else:
        print(f"After {num_attempts} tries, the greatest local maximum discovered was {best_local_max}. The actual global maximum was {global_max}.")

        
if __name__ == "__main__":
    # uncomment code block for hillClimb testing 
    #print("=" * 120)
    #unittest.main(argv=[''], exit=False)
    #print("=" * 120)

    print("")
    print("=" * 120)
    main()
    print("=" * 120)
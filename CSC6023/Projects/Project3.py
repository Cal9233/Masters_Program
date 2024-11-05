def tribo(n, values):
  """
  Calculate the nth element of the Tribonacci sequence using dynamic programming.

  Args:
  n (int): The position in the sequence to calculate (1-based indexing)
  
  Returns:
  int: The nth number in the Tribonacci sequence
  """
  # If n is within our known values, return directly
  if n < len(values):
      return values[n]
  # For values beyond our initial sequence, calculate using dynamic programming
  ans = (tribo(n-1, values) + tribo(n-2, values) + tribo(n-3, values))
  values += [ans]
  return ans

def main():
  """
  Main function that handles user interaction for calculating Tribonacci numbers.
  Continuously prompts user for input until a number less than 1 is entered.
  Handles invalid inputs by catching ValueError exceptions.
  """
  while True:
    try:
      # Get user input and convert to integer
      n = int(input("Please input a positive integer: "))
      
      # Exit condition
      if n < 1:
          break
      
      # Initialize dp array with first 9 known values from requirements
      tribo_seq = [1, 1, 1, 3, 5, 9, 17, 31, 57]
      result = tribo(n - 1, tribo_seq)
      print(f"The {n}-th element of Tribonacci is {result}.")
      
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
  main()
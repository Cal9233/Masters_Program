def tribo(n):
  """
  Calculate the nth element of the Tribonacci sequence using dynamic programming.
  The sequence starts with [1,1,1] where each subsequent number is the sum of the previous three.

  Args:
      n (int): The position in the sequence to calculate (1-based indexing)
      
  Returns:
      int: The nth number in the Tribonacci sequence
      None: If n <= 0
  """
  if n <= 0:
    return None

  # Initialize dp array with first 9 known values from requirements
  tribo_seq = [1, 1, 1, 3, 5, 9, 17, 31, 57]

  # If n is within our known values, return directly
  if n <= len(tribo_seq):
    return tribo_seq[n - 1]

  # For values beyond our initial sequence, calculate using dynamic programming
  for i in range(len(tribo_seq), n):
    tribo_seq.append(tribo_seq[i - 1] + tribo_seq[i - 2] + tribo_seq[i - 3])

  return tribo_seq[-1]

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
          
      result = tribo(n)
      print(f"The {n}-th element of Tribonacci is {result}.")
      
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
  main()
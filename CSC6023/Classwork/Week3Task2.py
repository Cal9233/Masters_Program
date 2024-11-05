def calculate_min_moves(n):
  """
  Calculate the minimum number of moves required to solve the Towers of Hanoi puzzle
  for n disks.
  
  Args:
      n (int): Number of disks
      
  Returns:
      int: Minimum number of moves required
  """
  # Base case: 0 or 1 disk
  if n <= 1:
    return n
  
  # Recursive case: 2^n - 1
  return 2 * calculate_min_moves(n - 1) + 1

def main():
  while True:
    try:
        n = int(input("\nPlease input the number of disks: "))
        if n < 0:
            print("Error: Number of disks cannot be less than zero. Please try again.")
            continue
            
        min_moves = calculate_min_moves(n)
        print(f"\nMinimum number of moves required: {min_moves}")
        
        # Ask if user wants to try again
        again = input("\nWould you like to try another number? (y/n): ").lower()
        if again != 'y':
            break
            
    except ValueError as e:
        if "invalid literal for int()" in str(e):
            print("Error: Please enter a valid integer.")
        else:
            print(f"Error: {e}")


if __name__ == "__main__":
  main()
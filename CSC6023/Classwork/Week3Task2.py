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
  # For n disks, we need to:
  # 1. Move n-1 disks to auxiliary peg
  # 2. Move largest disk to target peg
  # 3. Move n-1 disks from auxiliary to target peg
  return (2 ** n) - 1

def tower_of_hanoi(n, from_, aux_, to_):
  """
  Recursive function to solve Tower of Hanoi puzzle.
  
  Args:
      n (int): Number of disks
      from_ (str): Source peg
      aux_ (str): Auxiliary peg
      to_ (str): Target peg
  """
  if n == 1:
    print(f"Move disk 1 from {from_} to {to_}.")
    return
  
  # Move n-1 disks from source to auxiliary peg
  tower_of_hanoi(n - 1, from_, to_, aux_)
    
  # Move the largest disk from source to target peg
  print(f"Move disk {n} from {from_} to {to_}")
  
  # Move n-1 disks from auxiliary to target peg
  tower_of_hanoi(n - 1, aux_, from_, to_)

def main():
  while True:
    try:
        n = int(input("\nPlease input the number of disks: "))
        if n < 0:
            print("Error: Number of disks cannot be less than zero. Please try again.")
            continue
            
        min_moves = calculate_min_moves(n)
        print(f"\nMinimum number of moves required: {min_moves}")
        print("\nHere are the steps to solve:")
        tower_of_hanoi(n, "A", "B", "C")  # Fixed: Added missing 'n' parameter
        
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
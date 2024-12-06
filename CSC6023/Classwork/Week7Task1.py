import random

def balance_random_list(size):
  """
  Creates an array with 0's and 1's, both elements are equal in count length.

  Args:
  size (int): The amount for array size.
  
  Returns:
  result (array): The array filled with 0's and 1's, elements are randomly shuffled.
  """
  result = [0] * (size // 2) + [1] * (size // 2)
  random.shuffle(result) # Shuffles order of elements
  return result

def LasVegas(arr):
  """
  Las Vegas Algorithm which randomly selects an element in array, returns element 
  and index position if condition is met.

  Args:
  arr (array): An array containing randomly shuffled 1's and 0's.

  Returns:
  tries (int): Attempts it took to meet condition.
  index (int): Index position of element that meets condition.
  """
  tries = 0
  while True:
    tries += 1
    i = random.randint(0, len(arr) - 1)
    if arr[i] == 1:
      return tries, i

def main():
  """
  Main function that creates the randomly generated array and runs the Las Vegas Algorithm.
  """
  randlist = balance_random_list(10000)
  attempts, index = LasVegas(randlist)

  print("Las Vegas Algorithm Task")
  print("------------------------")
  print("")
  print(f"It took {attempts} attempts to randomly select 1 in the array.")
  print(f"Found at index {index} of the array.")
  print("")
  print("------------------------")

if __name__ == "__main__":
  # Runs program
  main()
import random

class DoubleArrayQueue:
  def __init__(self):
    """Initialize the double array queue with tracking counters."""
    self.array_in = []
    self.array_out = []
    self.cheap = 0
    self.costly = 0
  
  def enqueue(self, n):
    """ 
    Add an element to the queue.
    This is a cheap operation (O(1)).
    """
    self.array_in.append(n)
    self.cheap += 1

  def dequeue(self):
    """
    Remove and return an element from the queue.
    Cheap (O(1)) unless array_out is empty.
    """
    try:
      if self.array_out == []:
        for n in self.array_in:
          self.array_out.append(n)
        self.costly += 1
        self.array_in = []
      return self.array_out.pop(0)
    except IndexError:
      raise IndexError("Can't dequeue from an empty queue.")
    
  def operation_prbability(self):
    """
    Returns the total and percentage of cheap and costly operations.
    """
    total_op = self.cheap + self.costly
    cheap_perc = (self.cheap / total_op * 100) if total_op > 0 else 0
    costly_perc = (self.costly / total_op * 100) if total_op > 0 else 0
    return {
      'cheap': self.cheap,
      'costly': self.costly,
      'cheap_percentage': cheap_perc,
      'costly_percentage': costly_perc
    }

  
def ratio ():
  """
  Get valid enqueue/dequeue ratios from user input.
  Ensures ratios are between 34% and 66%.
  """
  while True:
    try:
      enqueue = float(input("Enter probability of enqueue operations (34-66): "))
      if 34 <= enqueue <= 66:
        dequeue = 100 - enqueue
        return enqueue/100, dequeue/100
      else:
        print("Error: Probability must be between 34 and 66")
    except ValueError:
      print("Please enter a valid number")

def randomize_operation(q, enq_prob, num_op = 100000):
  """
  Simulate queue operations based on given probability.
  
  Arguments:
    queue: DoubleArrayQueue instance
    enqueue_prob: Probability of enqueue operation
    num_operations: Total number of operations to perform
  """
  for _ in range(num_op):
    if random.random() < enq_prob:
      q.enqueue(random.randint(1, 100))
    else:
      try:
        q.dequeue()
      except IndexError:
        q.enqueue(random.randint(1, 100))

def main():
  # Initialize DoubleArrayQueue class
  q = DoubleArrayQueue()
  # Get user-defined ratio
  en, de = ratio()
  print(f"\nProbabilities set to:")
  print(f"Enqueue: {en*100:.1f}%")
  print(f"Dequeue: {de*100:.1f}%")
  
  # Simulate operations
  print("\nSimulating 100,000 operations...")
  randomize_operation(q, en)
  
  # Get and display statistics
  stats = q.operation_prbability()
  print("\nOperation Statistics:")
  print(f"Cheap operations: {stats['cheap']} ({stats['cheap_percentage']:.2f}%)")
  print(f"Costly operations: {stats['costly']} ({stats['costly_percentage']:.2f}%)")
  
if __name__ == "__main__":
  main()
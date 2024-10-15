# Exercise: Implement a Task Manager using Stack and Queue

# 1. Implement a Stack class with the following methods:
#    - push(item): Add an item to the top of the stack
#    - pop(): Remove and return the top item from the stack
#    - peek(): Return the top item without removing it
#    - is_empty(): Return True if the stack is empty, False otherwise

class Stack:
    # Your implementation here
  def __init__(self):
    self.items = []

  def push(self, item):
    if item == None:
      print("No item.")
    else:
      self.items.append(item)
      print(f"Item pushed.")

  def is_empty(self):
    return len(self.items) == 0
    
  def peek(self):
    if self.is_empty():
      return None
    else:
      return self.items[-1]
    
  def pop(self):
    if self.is_empty():
      print("Currently no tasks.")
    else:
      top_item = self.items.pop()
      return top_item
    
  def print(self):
    if self.is_empty():
      print("Currently no urgent tasks.")
    else:
      for item in self.items:
        print(str(item))
      
# 2. Implement a Queue class with the following methods:
#    - enqueue(item): Add an item to the back of the queue
#    - dequeue(): Remove and return the front item from the queue
#    - front(): Return the front item without removing it
#    - is_empty(): Return True if the queue is empty, False otherwise

class Queue:
    # Your implementation here
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    if item == None:
      print("No item.")
    else:
      self.items.append(item)
      print(f"Inserting item.")

  def is_empty(self):
    return len(self.items) == 0
  
  def dequeue(self):
    if self.is_empty():
      print("Queue is currently empty.")
    else:
      dequeue_item = self.items.pop(0)
      return dequeue_item

  def front(self):
    if self.is_empty():
      print("Queue is currently empty.")
    else:
      return self.items[0]
    
  def print(self):
    if self.is_empty():
      print("Currently no regular tasks.")
    else:
      for item in self.items:
        print(str(item))
# 3. Implement a TaskManager class that uses both Stack and Queue:
#    - The TaskManager should have a stack for "urgent" tasks and a queue for "regular" tasks
#    - Implement the following methods:
#      * add_task(task): Add a task to the urgent stack or regular queue
#      * complete_task(task): Mark task
#      * complete_task(): Complete the next task (urgent tasks have priority)
#      * display_tasks(): Display all tasks (both urgent and regular)

class TaskManager:
    # Your implementation here
  def __init__(self):
    self.regular_tasks = Queue()
    self.urgent_tasks = Stack()

  def add_task(self, description, isUrgent = False):
    task = Task(description, isUrgent)
    if isUrgent:
      print(f"Adding urgent task to Stack.")
      self.urgent_tasks.push(task)
    else:
      print(f"Adding regular task to queue.")
      self.regular_tasks.enqueue(task)

  def complete_task(self):
    if not self.urgent_tasks.is_empty():
      task = self.urgent_tasks.pop()
    elif not self.regular_tasks.is_empty():
      task = self.regular_tasks.dequeue()
    else:
      print("No tasks to complete.")
      return None
    
    task.mark_complete()
    return task

  def display_tasks(self):
      if self.regular_tasks.is_empty() and self.urgent_tasks.is_empty():
          print("Task Manager currently has no tasks.")
      else:
          print("Tasks:")
          print("Urgent tasks:")
          self.urgent_tasks.print()
          print("Regular tasks:")
          self.regular_tasks.print()

class Task:
  def __init__(self, description, isUrgent = False):
    self.description = description
    self.completed = False
    self.isUrgent = isUrgent

  def mark_complete(self):
    self.completed = True

  def __str__(self):
    status = "Completed" if self.completed else "Pending"
    urgency = "Urgent Task" if self.isUrgent else "Regular"
    return f"{self.description} - status: {status} ({urgency})"
# 4. Write a main function to demonstrate the TaskManager:
#    - Add some urgent and regular tasks
#    - Display all tasks
#    - Complete a few tasks
#    - Display the remaining tasks

def main():
  # Your implementation here
  task_manager = TaskManager()
  task_manager.add_task("Finish this program")
  task_manager.add_task("Work out", True)

  print("Initial tasks: ")
  task_manager.display_tasks()

    # Completing tasks
  print("\nCompleting tasks:")
  for _ in range(3):
      completed_task = task_manager.complete_task()
      if completed_task:
          print(f"Completed: {completed_task}")

  print("\nRemaining tasks:")
  task_manager.display_tasks()

if __name__ == "__main__":
  main()
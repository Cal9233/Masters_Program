from typing import Self, Typevar
# Reject duplicates for insert methods
# Binary searh tree or hash can be used for concepts of map
# Hash table is faster unless it starts to get full
# Hash : O(1)   Tree: O(log n)

#region (comment that can collapse)

# tree of integers


# left and right pointers
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

# add function
# contains function
class Tree:
  def __init__(self):
    self.root = None
    self.height = 0

  def contain(self):
    if self.root == None:
      return
    
    print(self.root)
    self.contain(self.left)
    self.contain(self.right)

  def add(self, data):
    if self.root is None:
      self.root = data
      self.left = Tree()
      self.right = Tree()
      self.height += 1
      print(f"{data} is successfully added.")

    elif self.root < data:
      self.right.add(data)

    elif self.root > data:
      self.left.add(data)

    elif self.root == data:
      return

n = Node(5)
t = Tree()
t.add(n)
t.contain()
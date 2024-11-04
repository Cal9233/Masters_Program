# A Tree is a Hierarchical structure that is a collection of nodes that are connected by edges
# Root: Topmost node of the tree
# Children: Bottom portion of the Root
# Each node can have multiple child nodes, and child nodes can also have child notes making this a recursive structure
# A Tree is a non-linear data structure, they are arranged on multiple levels
# Leaf/External Nodes: Nodes with no child nodes
# Example:

class TreeNode:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def insert_into_tree(root, value):
  if root is None:
    return TreeNode(value)
  if value < root.value:
    root.left = TreeNode(root.left, value)
  else:
    root.right = TreeNode(value, root.right)
  return root


# Exercise:
# Create Luna's family:

# Luna (parent dog)
# Max (baby dog on the left)
# Bella (baby dog on the right)

# Who is Max and Bella's parent?
# How many babies does Luna have?
# What type of pet is Max?


#        Luna (dog)
#      /          \
#   Max (dog)   Bella (dog)
#    /
#Rocky (dog)


#CHALLENGE:
#Can you write code to:

#Add a baby pet to Bella
#Print all the pet names in the family

class PetTree:
  def __init__(self, pet_name, pet_type):
    self.pet_name = pet_name
    self.pet_type = pet_type
    self.left = None
    self.right = None

  def __str__(self):
    children = []
    if self.left: children.append(self.left.pet_name)
    if self.right: children.append(self.right.pet_name)
    return f"Pet: {self.pet_name} ({self.pet_type}) - Babies: {', '.join(children) if children else 'none'}"
  
  def __repr__(self):
    return f"PetTree(name='{self.pet_name}', type='{self.pet_type}')"
  
  def add_pet(self, parent_name, pet_name, pet_type):
    if self.pet_name == parent_name:
      if self.left is None:
        self.left = PetTree(pet_name, pet_type)
        return True
      elif self.right is None:
        self.right = PetTree(pet_name, pet_type)
        return True
      else:
        return False

    found = False
    if self.left:
      found = self.left.add_pet(parent_name, pet_name, pet_type)
    if not found and self.right:
      found = self.right.add_pet(parent_name, pet_name, pet_type)
    
    return found
        
  def print_pet_family(self):
    if self is None:
      return
    print(f"Pet Name: {self.pet_name}, Type: {self.pet_type}")

    print(self)
    # Print left baby
    if self.left:
      print(f"{self.pet_name}'s left baby is {self.left.pet_name}")
    # Print right baby
    if self.right:
      print(f"{self.pet_name}'s right baby is {self.right.pet_name}")
    
    if self.left:
      self.left.print_pet_family()
    if self.right:
      self.right.print_pet_family()

family = PetTree("Luna", "Dog")
family.left = PetTree("Max", "Dog")
family.right = PetTree("Bella", "Dog")
family.left.left = PetTree("Rocky", "Dog")

print("Initial family:")
family.print_pet_family()

print("\nAdding new pets:")
family.add_pet("Max", "Rocko", "Dog")  # Should add Rocko as Max's right baby
family.add_pet("Bella", "Oreo", "Dog")  # Should add Oreo as Bella's left baby
family.add_pet("Rocky", "Harold", "Dog")  # Should add Harold as Rocky's left baby

print("\nUpdated family:")
family.print_pet_family()
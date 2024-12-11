from typing import Self, TypeVar, Optional

T = TypeVar("T")

class Node[T]:
  def __init__(self, data: T):
    self.data : T = data
    self.left : Optional[Node[T]] = None
    self.right : Optional[Node[T]] = None

class Tree[T]:
  def __init__(self):
    self.root : Optional[Node[T]] = None
    self.height : int = 0

  def _add(self, data : T) -> Self:
    if self.root is None:
      self.root = Node(data)
      self.height += 1
      return self
    
    current = self.root
    while True:
      if data < current.data:
        if current.left is None:
          current.left = Node(data)
          self.height += 1
          break
        current = current.left
      elif data > current.data:
        if current.right is None:
          current.right = Node(data)
          self.height += 1
          break
        current = current.right
      else:
        break

    return self

  def _contains(self, target : T) -> bool:
    current = self.root
    while current is not None:
      if current.data == target:
        return True
      elif current.data > target:
        current = current.left
      else:
        current = current.right
    return False


def main():
  tree = Tree[int]()
  tree._add(1)._add(5)._add(10)
  print("Tree contents:")
  print(f"\nContains 7? {tree._contains(7)}")
  print(f"Contains 10? {tree._contains(10)}")


if __name__ == "__main__":
  main()
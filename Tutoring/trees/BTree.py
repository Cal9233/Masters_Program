from typing import Self, TypeVar, Callable, Optional, Any

def default_compare(left: Any, right: Any):
    if left == right:
        return 0
    elif left < right:
        return -1
    else:
        return 1

T = TypeVar("T")
    
class Node[T]:
    data: T
    left: Self | None
    right: Self | None
    
    def __init__(self, data: T):
        self.data = data
        self.left = None
        self.right = None

    # def _display_aux(self):
    #     # No child.
    #     if self.right is None and self.left is None:
    #         line = '%s' % self.data
    #         width = len(line)
    #         height = 1
    #         middle = width // 2
    #         return [line], width, height, middle

    #     # Only left child.
    #     if self.right is None:
    #         lines, n, p, x = self.left._display_aux()
    #         s = '%s' % self.data
    #         u = len(s)
    #         first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
    #         second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
    #         shifted_lines = [line + u * ' ' for line in lines]
    #         return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    #     # Only right child.
    #     if self.left is None:
    #         lines, n, p, x = self.right._display_aux()
    #         s = '%s' % self.data
    #         u = len(s)
    #         first_line = s + x * '_' + (n - x) * ' '
    #         second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
    #         shifted_lines = [u * ' ' + line for line in lines]
    #         return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    #     # Two children.
    #     left, n, p, x = self.left._display_aux()
    #     right, m, q, y = self.right._display_aux()
    #     s = '%s' % self.data
    #     u = len(s)
    #     first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    #     second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    #     if p < q:
    #         left += [n * ' '] * (q - p)
    #     elif q < p:
    #         right += [m * ' '] * (p - q)
    #     zipped_lines = zip(left, right)
    #     lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    #     return lines, n + m + u, max(p, q) + 2, n + u // 2

class Tree[T]:
    _root: Node[T] | None
    _height: int
    _compare: Callable[[T, T], int]
    
    def __init__(self, compare: Optional[Callable[[T, T], int]] = None):
        self._root = None
        self._height = 0
        self._compare = compare if compare is not None else default_compare

    def add(self, data: T) -> bool:
        if self._root is None:
            self._root = Node(data)
            self._height = 1
            return True
        
        def add_r(root: Node[T], data: T, height: int) -> tuple[bool, int]:
            comparison = self._compare(data, root.data)
            if comparison < 0:
                if root.left is None:
                    root.left = Node(data)
                    return True, height
                else:
                    return add_r(root.left, data, height + 1)   
            elif comparison > 0:
                if root.right is None:
                    root.right = Node(data)
                    return True, height
                else:
                    return add_r(root.right, data, height + 1)
            else:
                return False, 0
        
        success, new_h = add_r(self._root, data, 2)

        if success:
            self._height = new_h
            return True
        else:
            return False
    
    def contains(self, target: T) -> bool:
        if self._root is None:
            return False

        def contains_r(root: Node[T], target: T) -> bool:
            comparison = self._compare(target, root.data)
            if comparison < 0:
                return False if root.left is None else contains_r(root.left, target)
            elif comparison > 0:
                return False if root.right is None else contains_r(root.right, target)
            else:
                return True
        
        return contains_r(self._root, target)
    
    def remove(self, target: T) -> bool:
        if self._root is None:
            return False
        
        def find_node(root: Node[T] | None, parent: Node[T] | None, target: T) -> tuple[Node[T], Node[T] | None] | None:
            if root is None:
                return None
            
            comparison = self._compare(target, root.data)
            
            if comparison < 0:
                return find_node(root.left, root, target)
            elif comparison > 0:
                return find_node(root.right, root, target)
            else:
                return (root, parent)

        def remove_node(node: Node[T], parent: Node[T] | None):
            # If node is leaf, disconnect from parent
            if node.left is None and node.right is None:
                if parent is not None:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self._root = None
            
            # If node has two children, replace with smallest node in right subtree
            elif node.left is not None and node.right is not None:
                successor_parent = node
                successor = node.right
                while successor.left:
                    successor_parent = successor
                    successor = successor.left

                # Replace node's value with successor's value
                node.data = successor.data

                # Remove successor from its original position
                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right

            # If node has one child, replace with child
            else:
                child = node.left if node.left is not None else node.right 
                if parent is not None:
                    if parent.left == node:
                        parent.left = child 
                    else:
                        parent.right = child
                else:
                    self._root = child

        result = find_node(self._root, None, target)
        if result is None:
            return False
        child, parent = result
        remove_node(child, parent)
        return True
    
    def print(self):
        def print_node(node: Node[T] | None, level: int):
            if node is None:
                return
            else:
                for i in range(0, level):
                    print("|-" if i == level-1 else "    ", end = "")
                print(node.data)
                print_node(node.left, level + 1)
                print_node(node.right, level + 1)
        
        print_node(self._root, 0)
        

    # def display(self):
    #     if self._root is None:
    #         print("Empty tree")
    #         return
    #     lines, *_ = self._root._display_aux()
    #     for line in lines:
    #         print(line)

def main():
    tree = Tree[int]()
    tree.add(5)
    tree.add(3)
    tree.add(9)
    tree.add(1)
    tree.add(2)
    tree.add(6)
    tree.add(12)
    print("Tree contents:")
    tree.print()

    print(f"\nContains 7? {tree.contains(7)}")
    print(f"Contains 6? {tree.contains(6)}")
    print(f"Removing 9 {tree.remove(9)}")
    print(f"Contains 9? {tree.contains(9)}")
    print("\nAfter removal:")
    tree.print()

    print(f"Removing 3 {tree.remove(3)}")
    print(f"Contains 3? {tree.contains(3)}")
    print("\nAfter removal:")
    tree.print()

if __name__ == "__main__":
    main()
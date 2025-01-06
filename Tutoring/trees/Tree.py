from random import randint, shuffle

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self)

    def add_child(self, item):
        self.children.append(Node(item))

    def print(self, level = 0):
        for i in range(0, level):
            print("|-" if i == level-1 else "    ", end = "")
        print(self.data)
        for child in self.children:
            child.print(level + 1)

def build_tree() -> Node:
    
    def bt_r(node: Node, numbers: list[int], depth: int):

        if(depth > 4):
            return

        for _ in range(0, randint(1, 3)):
            if len(numbers) == 0:
                break
            node.add_child(numbers.pop())
        
        for child in node.children:
            bt_r(child, numbers, depth + 1)
    
    numbers = list(range(1, 101))
    shuffle(numbers)
    root = Node(numbers.pop())
    bt_r(root, numbers, 0)
    return root


def findLongestPath(root, target):
    paths = []
    def dfs(node, path):
        new_path = list(path)
        new_path.append(node)
        if node.data == target:
            paths.append(new_path)
            return
        else:
            for child in node.children:
                dfs(child, new_path)
    dfs(root, [])
    largest = max(paths, key = lambda lst: len(lst))
    return largest

root = build_tree()
print("Tree: ")
root.print()
longest = findLongestPath(root, 45)
print(longest)
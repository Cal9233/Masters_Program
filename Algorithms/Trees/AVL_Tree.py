class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self, root, data):
        pass

    def insert_node(self, root, data):
        pass

def main():
    myTree = AVL()
    root = None
    a = [33, 13, 52, 9, 21, 61, 8, 11]
    for d in a:
        root = myTree.insert_node(root, d)
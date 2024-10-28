class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        self.update_height(y)
        self.update_height(x)
        
        return x
    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        self.update_height(x)
        self.update_height(y)
        
        return y
    
    def insert(self, root, key):
        if not root:
            return Node(key)
            
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root
        
        self.update_height(root)
        
        balance = self.balance_factor(root)
        
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def insert_key(self, key):
        self.root = self.insert(self.root, key)
    
    def post_order_traversal(self, node, result):
        """Helper method to perform post-order traversal recursively"""
        if not node:
            return
        
        # First traverse left subtree
        self.post_order_traversal(node.left, result)
        
        # Then traverse right subtree
        self.post_order_traversal(node.right, result)
        
        # Finally, add the current node's key
        result.append(node.key)
    
    def print_post_order(self):
        """Public method to print the tree in post-order traversal"""
        result = []
        self.post_order_traversal(self.root, result)
        print("Post-order traversal:", result)
        return result

def main():
    # Create an AVL tree
    avl = AVLTree()
    
    # Insert some values
    values = [10, 5, 15, 3, 7, 12, 18]
    print("Inserting values:", values)
    
    for value in values:
        avl.insert_key(value)
    
    # Perform and print post-order traversal
    avl.print_post_order()

if __name__ == "__main__":
    main()
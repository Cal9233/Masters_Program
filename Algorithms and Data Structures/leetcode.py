class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # we want to visit node, move left nodes to right, and move right nodes to outer right
        if root is None:
            return root
            
        res = []
        nodes_list = [root]

        while len(nodes_list) > 0:
            curr_node = nodes_list.pop()
            res.append(curr_node.val)
            if curr_node.right:
                nodes_list.append(curr_node.right)
            if curr_node.left:
               nodes_list.append(curr_node.left)

        new_tree = TreeNode(res[0], None, None)
        pointer = new_tree
        for i in range(1, len(res)):
            pointer.right = TreeNode(res[i], None, None)
            pointer = pointer.right

        root = new_tree

def list_to_tree(nums):
    if not nums or nums[0] is None:
        return None
    
    root = TreeNode(nums[0])
    queue = [root]
    i = 1
    
    while queue and i < len(nums):
        node = queue.pop(0)
        
        # Left child
        if i < len(nums) and nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    

# Initialize the tree
input_list = [1, 2, 5, 3, 4, None, 6]
root = list_to_tree(input_list)
sol = Solution()
print(sol.flatten(root))
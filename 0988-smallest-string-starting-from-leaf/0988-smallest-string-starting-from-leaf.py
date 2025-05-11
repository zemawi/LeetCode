# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.smallest = "~"  
        def dfs(node, path):
            if not node:
                return
            
            
            current_char = chr(ord('a') + node.val)
            path = current_char + path

            
            if not node.left and not node.right:
                if path < self.smallest:
                    self.smallest = path

           
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return self.smallest

        
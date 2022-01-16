# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        self.helper(root, path)
        return path
    
    def helper(self, node, path):
        if not node:
            return 
        self.helper(node.left, path)
        path.append(node.val)
        self.helper(node.right, path)
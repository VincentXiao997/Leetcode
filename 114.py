# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        self.helper(node)
        
    def helper(self, node):
        if not node:
            return None
        if not node.right and not node.left:
            return node
        
        rightLast = self.helper(node.right)
        leftLast = self.helper(node.left)
        
        if leftLast:
            leftLast.right = node.right
            node.right = node.left
            node.left = None
        
        if rightLast:
            return rightLast
        else: 
            return leftLast
 
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.helper(root, low, high)
    
    def helper(self, node, low, high):
        if not node:
            return 0
        
        if node.val == high:
            return node.val + self.helper(node.left, low, high)
        if node.val == low:
            return node.val + self.helper(node.right, low, high)
        if node.val < low:
            return self.helper(node.right, low, high)
        if node.val > high:
            return self.helper(node.left, low, high)
        
        return node.val + self.helper(node.left, low, high) + self.helper(node.right, low, high)
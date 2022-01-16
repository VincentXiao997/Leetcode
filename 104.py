# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, node, depth):
        if not node:
            return depth
        leftDepth = self.dfs(node.left, depth + 1)
        rightDepth = self.dfs(node.right, depth + 1)
        if leftDepth > rightDepth:
            return leftDepth
        else:
            return rightDepth
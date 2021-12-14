# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:
            return self.dfs(root, p.val, q.val)
        else:
            return self.dfs(root, q.val, p.val)
        
    def dfs(self, node, p, q):
        if not node:
            return None
        if node.val >= p and node.val <= q:
            return node
        elif node.val > q:
            return self.dfs(node.left, p, q)
        else:
            return self.dfs(node.right, p, q)
        
        
        
        
            
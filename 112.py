# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# stack + dfs
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, pathSum = stack.pop()
            if not node.left and not node.right and pathSum == targetSum:
                return True
            if node.right:
                stack.append((node.right, pathSum + node.right.val))
            if node.left:
                stack.append((node.left, pathSum + node.left.val))
        return False
# recursion 
class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, 0, targetSum)
        
    def dfs(self, node, pathSum, targetSum):
        if not (node.left or node.right) and node.val + pathSum == targetSum:
            return True
        
        if node.left and self.dfs(node.left, pathSum + node.val, targetSum):
            return True
        if node.right and self.dfs(node.right, pathSum + node.val, targetSum):
            return True
        
        return False
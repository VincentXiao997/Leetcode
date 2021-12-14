# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dfs(root, [])
    
    def dfs(self, node, path):
        if not node:
            return None
        path.append(str(node.val))
        
        leftResult = self.dfs(node.left, path)
        rightResult = self.dfs(node.right, path)
        
        if not leftResult and not rightResult:
            result = int("".join(path))
            path.pop()
            return result
        elif leftResult and rightResult:
            path.pop()
            return leftResult + rightResult
        elif leftResult:
            path.pop()
            return leftResult
        else:
            path.pop()
            return rightResult
        
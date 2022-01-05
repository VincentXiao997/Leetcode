# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([])
        queue.append(root)
        while queue:
            n = len(queue)
            deepestSum = 0
            for _ in range(n):
                node = queue.popleft()
                deepestSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return deepestSum
                    
# DFS

class Solution_DFS:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        sumVal, _ = self.dfs(root, 0)
        return sumVal
    
    def dfs(self, node, depth):
        if not node.left and not node.right:
            return node.val, depth
        
        leftSum, rightSum, leftDepth, rightDepth = None, None, None, None
        if node.left:
            leftSum, leftDepth = self.dfs(node.left, depth + 1)
        if node.right:
            rightSum, rightDepth = self.dfs(node.right, depth + 1)
        
        if leftSum and rightSum:
            if leftDepth == rightDepth:
                return leftSum + rightSum, leftDepth 
            elif leftDepth > rightDepth:
                return leftSum, leftDepth
            else:
                return rightSum, rightDepth
        elif leftSum:
            return leftSum, leftDepth
        else:
            return rightSum, rightDepth
                    
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        minLevel = -1
        maxSum = -math.inf
        level = 1
        while queue:
            n = len(queue)
            curSum = 0
            for _ in range(n):
                node = queue.popleft()
                curSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if curSum >  maxSum:
                maxSum = curSum
                minLevel = level
            level += 1
        return minLevel
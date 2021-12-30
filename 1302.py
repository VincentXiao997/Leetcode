# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
                    
                
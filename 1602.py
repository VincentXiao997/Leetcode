# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        queue = collections.deque([root])
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.val == u.val:
                    if i + 1 < n:
                        return queue.popleft()
                    else:
                        return None
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return None
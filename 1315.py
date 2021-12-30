# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0
        queue = collections.deque([])
        queue.append(root)
        evenParentQueue = collections.deque([])
        result = 0
        while queue or evenParentQueue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.val % 2 == 0:
                    if node.left:
                        evenParentQueue.append(node.left)
                    if node.right:
                        evenParentQueue.append(node.right)
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            n = len(evenParentQueue)
            for _ in range(n):
                node = evenParentQueue.popleft()
                if node.val % 2 == 0:
                    if node.left:
                        result += node.left.val
                        evenParentQueue.append(node.left)
                    if node.right:
                        result += node.right.val
                        evenParentQueue.append(node.right)
                else:
                    if node.left:
                        result += node.left.val
                        queue.append(node.left)
                    if node.right:
                        result += node.right.val
                        queue.append(node.right)
        return result
            
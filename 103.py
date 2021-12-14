# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        isOdd = True
        results = []
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            layer = []
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if isOdd:
                    layer.append(node.val)
                else:
                    layer = [node.val] + layer
            results.append(layer)
            isOdd = not isOdd
        return results
                    
                    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        node = root
        results = []
        queue = collections.deque([node])
        while queue:
            size = len(queue)
            currentLayer = []
            for _ in range(size):
                currentLayer.append(queue.popleft())
            results.append(currentLayer[-1].val)
            for node in currentLayer:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return results
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = collections.deque([root])
        result = []
        if not root:
            return result
        while queue:
            n = len(queue)
            curLayer = []
            for _ in range(n):
                node = queue.popleft()
                curLayer.append(node.val)
                for child in node.children:
                    queue.append(child)
            result.append(curLayer)
        return result
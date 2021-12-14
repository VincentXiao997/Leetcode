# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        resultSet = {}
        results = []
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, virticalIndex = queue.popleft()
            if not node:
                continue
            if virticalIndex in resultSet:
                resultSet[virticalIndex].append(node.val)
            else:
                resultSet[virticalIndex] = [node.val]
            if node.left:
                queue.append((node.left, virticalIndex - 1))
            if node.right:
                queue.append((node.right, virticalIndex + 1))
            
        sortedKeys = list(resultSet.keys())
        sortedKeys.sort()
        for i in sortedKeys:
            results.append(resultSet[i])
        return results
    
    
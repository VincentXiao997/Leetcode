# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.bfs(root, 0)
        return root
        
    def bfs(self, node, greatSumAbove):
        if not node:
            return 0
        rightSum = self.bfs(node.right, greatSumAbove)
        leftSum = self.bfs(node.left, greatSumAbove + rightSum + node.val)
        returnSum = node.val + rightSum + leftSum
        node.val += (rightSum + greatSumAbove)
        return returnSum
        
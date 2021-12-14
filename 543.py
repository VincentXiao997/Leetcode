# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLen, _ = self.dfs(root)
        return maxLen
    def dfs(self, node):
        if not node:
            return 0, -1
        leftMax, leftLen = self.dfs(node.left)
        rightMax, rightLen = self.dfs(node.right)
        length = 1
        if leftLen > rightLen:
            length += leftLen
        else:
            length += rightLen
        maxLength = leftLen + rightLen + 2
        if maxLength < leftMax:
            maxLength = leftMax
        if maxLength < rightMax:
            maxLength = rightMax
        return maxLength, length
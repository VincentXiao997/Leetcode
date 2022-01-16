# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        self.dfs(root, [], paths)
        return paths
    
    def dfs(self, node, curPath, paths):
        if not node:
            return
        if not node.left and not node.right:
            paths.append("->".join(curPath + [str(node.val)]))
            return
        self.dfs(node.left, curPath + [str(node.val)], paths)
        self.dfs(node.right, curPath + [str(node.val)], paths)
        
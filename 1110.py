# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        results = []
        self.delete(root, to_delete, results, True)
        return results
    
    def delete(self, node, to_delete, results, no_parent):
        if not node:
            return
        if not node.val in to_delete:
            if no_parent:
                results.append(node)
            self.delete(node.left, to_delete, results, False)
            self.delete(node.right, to_delete, results, False)
            if node.left and node.left.val in to_delete:
                node.left = None
            if node.right and node.right.val in to_delete:
                node.right = None
        else:
            left = node.left
            right = node.right
            node.left = None
            node.right = None
            self.delete(left, to_delete, results, True)
            self.delete(right, to_delete, results, True)
            
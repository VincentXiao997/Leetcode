# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        newTree = TreeNode()
        stack = [(root1, root2, newTree)]

        while stack:
            node1, node2, newNode = stack.pop()
            # print(node1, node2)
            # print("**********")
            if node1 and node2:
                newNode.val = node1.val + node2.val
                if node1.left or node2.left:
                    newNode.left = TreeNode()
                    stack.append((node1.left, node2.left, newNode.left))
                if node1.right or node2.right:
                    newNode.right = TreeNode()
                    stack.append((node1.right, node2.right, newNode.right))
            elif node1:
                # print(node1)
                newNode.val = node1.val
                if node1.left:
                    # print(node1.left)
                    newNode.left = TreeNode()
                    stack.append((node1.left, None, newNode.left))
                if node1.right:
                    newNode.right = TreeNode()
                    stack.append((node1.right, None, newNode.right))
            elif node2:
                newNode.val = node2.val
                if node2.left:
                    newNode.left = TreeNode()
                    stack.append((None, node2.left, newNode.left))
                if node2.right:
                    newNode.right = TreeNode()
                    stack.append((None, node2.right, newNode.right))
        return newTree
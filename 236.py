# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        _, _, commonAncestor = self.helper(root, p, q)
        # print("result", commonAncestor)
        return commonAncestor
    
    def helper(self, node, p, q):
        if not node:
            # print("it is none")
            return (False, False, None)
        # print(node.val)

        result = self.helper(node.left, p, q)
        # if node.left:
            # print(node.left.val)
            # print(result)
        leftFoundP, leftFoundQ, leftAncestor = result
        if leftFoundP and leftFoundQ:
            return (True, True, leftAncestor)
        rightFoundP, rightFoundQ, rightAncesotr = self.helper(node.right, p, q)
        # if node.right:
            # print(node.right.val)
            # print(rightFoundP, rightFoundQ, rightAncesotr)
        if rightFoundP and rightFoundQ:
            return (True, True, rightAncesotr)
        if (rightFoundP and leftFoundQ) or (rightFoundQ and leftFoundP):
            return True, True, node
        if node.val == p.val:
            if rightFoundQ or leftFoundQ:
                return (True, True, node)
            else:
                return (True, False, None)
        elif node.val == q.val:
            if rightFoundP or leftFoundP:
                return (True, True, node)
            else:
                return (False, True, None)
        else:
            if rightFoundQ or leftFoundQ:
                return (False, True, None)
            elif leftFoundP or rightFoundP:
                return (True, False, None)
            else:
                return (False, False, None)
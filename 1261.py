# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        queue = collections.deque([])
        root.val = 0
        queue.append(root)
        self.tree = set([0])
        while queue:
            node = queue.popleft()
            if node.left:
                node.left.val = node.val * 2 + 1
                queue.append(node.left)
                self.tree.add(node.left.val)
            if node.right:
                node.right.val = node.val * 2 + 2
                queue.append(node.right)
                self.tree.add(node.right.val)
            

    def find(self, target: int) -> bool:
        if target in self.tree:
            return True
        else:
            return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
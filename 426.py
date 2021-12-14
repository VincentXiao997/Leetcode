"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        smallest, largest = self.helper(root)
        smallest.left = largest
        largest.right = smallest
        return smallest
    
    def helper(self, node):
        if not node:
            return None, None
        smallestLeft, largestLeft = self.helper(node.left)
        smallestRight, largestRight = self.helper(node.right)
        if largestLeft:
            largestLeft.right = node
            node.left = largestLeft
        if smallestRight:
            node.right = smallestRight
            smallestRight.left = node
        
        smallest, largest = node, node
        if smallestLeft:
            smallest = smallestLeft
        if largestRight:
            largest = largestRight
        return smallest, largest 
            
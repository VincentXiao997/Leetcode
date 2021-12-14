"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# time complexity O(N)
# space complexity O(1)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        leftMost = root
        while leftMost:
            nextNode = None
            firstNode = None
            currentNode = leftMost
            while currentNode:
                if currentNode.left:
                    if not nextNode:
                        nextNode = currentNode.left
                        firstNode = currentNode.left
                    else:
                        nextNode.next = currentNode.left
                        nextNode = currentNode.left 
                if currentNode.right:
                    if not nextNode:
                        nextNode = currentNode.right
                        firstNode = currentNode.right
                    else:
                        nextNode.next = currentNode.right
                        nextNode = currentNode.right
                currentNode = currentNode.next
            leftMost = firstNode            
        return root
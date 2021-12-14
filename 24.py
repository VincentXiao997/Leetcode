# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next:
            backup = head.next
        else:
            return head
        firstNode, secondNode = None, None
        firstNode = head
        secondNode = head.next
        previousNode = None
        while firstNode and secondNode:
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            
            if previousNode:
                previousNode.next = secondNode
            previousNode = firstNode
            firstNode = firstNode.next
            if firstNode:
                secondNode = firstNode.next
        return backup
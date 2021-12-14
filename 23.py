# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i))
        # heap = [(lists[i].val, i) for i in range(len(lists))]
        listMap = {i: lists[i] for i in range(len(lists))}
        heapq.heapify(heap)
        sortedList = []
        smallestNode = None
        node = None
        while heap:
            val, index = heapq.heappop(heap)
            if not smallestNode:
                smallestNode = listMap[index]
                node = listMap[index]
            else:
                node.next = listMap[index]
                node = node.next
            if listMap[index].next:
                heapq.heappush(heap, (listMap[index].next.val, index))
                listMap[index] = listMap[index].next
        return smallestNode
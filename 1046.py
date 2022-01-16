class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-w for w in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            stone1, stone2 = heapq.heappop(heap), heapq.heappop(heap)
            if stone1 < stone2:
                heapq.heappush(heap, stone1 - stone2)
        if heap:
            return -heapq.heappop(heap)
        else:
            return 0
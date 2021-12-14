#  heap
# O(nlogk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for i in nums:
            if i in numMap:
                numMap[i] += 1
            else:
                numMap[i] = 1
        heap = [(numMap[key], key) for key in numMap]
        heapq._heapify_max(heap)
        result = []
        for _ in range(k):
            _, key = heapq._heappop_max(heap)
            result.append(key)
        return result
        
# quickselect
# O(N) worstcase O(N**2)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for i in nums:
            if i in numMap:
                numMap[i] += 1
            else:
                numMap[i] = 1
        heap = [(numMap[key], key) for key in numMap]
        return self.quickSelect(heap, len(heap)-k, 0, len(heap)-1)
    
    def quickSelect(self, numList, k, head, right):
        left, write = head, head
        mid = (left+right) // 2
        pivot = numList[mid][0]
        numList[mid], numList[right] = numList[right], numList[mid]
        while left < right:
            if numList[left][0] < pivot:
                numList[write], numList[left] =  numList[left], numList[write]
                write += 1
            left += 1
        numList[write], numList[right] = numList[right], numList[write]

        if write == k:
            return [element[1] for element in numList[k:]]
        elif write > k:
            return self.quickSelect(numList, k, head, write-1)
        else:
            return self.quickSelect(numList, k, write+1, right)
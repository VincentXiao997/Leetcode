class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missCounters = []
        for i, val in enumerate(arr):
            missCounters.append(val - i - 1)
        
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if missCounters[mid] < k:
                left = mid
            elif missCounters[mid] > k:
                right = mid
            else:
                right = mid
        if missCounters[right] < k:
            smallerIndex = right
        elif missCounters[left] < k:
            smallerIndex = left
        else:
            smallerIndex = -1
        if smallerIndex > -1:
            return arr[smallerIndex] + k - missCounters[smallerIndex]        
        else:
            return k
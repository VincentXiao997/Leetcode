

# heap O(nlogk)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)  # create a min-heap whose size is k 
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        # or use:
        # heapq.heappushpop(heap, num)
        return heap[0]

# quickSelect O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.select(nums, 0, len(nums) - 1, k - 1)
    
    def select(self, nums, left, right, k):
        storedIndex = self.partition(nums, left, right)

        if storedIndex == k:
            return nums[storedIndex]
        elif storedIndex > k:
            return self.select(nums, left, storedIndex - 1, k)
        else:
            return self.select(nums, storedIndex + 1, right, k)
    

    def partition(self, nums, left, right):
        pivotIndex = (left + right) // 2
        nums[right], nums[pivotIndex] = nums[pivotIndex], nums[right]
        storedIndex = left
        for i in range(left, right):
            if nums[i] > nums[right]:
                nums[i], nums[storedIndex] = nums[storedIndex], nums[i]
                storedIndex += 1
        nums[storedIndex], nums[right] = nums[right], nums[storedIndex]
        return storedIndex
          
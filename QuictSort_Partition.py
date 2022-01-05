class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.qSort(nums, 0, len(nums) - 1)
        return nums
           
    def qSort(self, nums, left, right):
        if left < right: 
            pi = self.partition(nums, left, right) 
            self.qSort(nums, left, pi-1) 
            self.qSort(nums, pi+1, right)
        
    def partition(self, nums, left, right):
        pivotIndex = random.randrange(left, right + 1)
        pivot = nums[pivotIndex]
        nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
        i, j = left, left
        while j < right:
            if nums[j] < pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1
            
        nums[i], nums[right] = nums[right], nums[i]
        return i
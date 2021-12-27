# two binary searches
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        minIndex = -1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        if nums[left] == target:
            minIndex = left
        elif nums[right] == target:
            minIndex = right
            
        left, right = 0, len(nums) - 1
        maxIndex = -1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[right] == target:
            maxIndex = right
        elif nums[left] == target:
            maxIndex = left
        
        if minIndex < 0 or maxIndex < 0:
            return False
        elif maxIndex - minIndex + 1 > len(nums) // 2:
            return True
        else:
            return False
        
        
# only one binary search function
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        a = self.binarySearch(nums, target + 1) 
        b = self.binarySearch(nums, target)
        length = a - b
        # print(a, b)
        if length > len(nums) // 2:
            return True
        else:
            return False
        
    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid 
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[right] < target:
            return right
        elif nums[left] < target:
            return left
        else:
            return -1
        
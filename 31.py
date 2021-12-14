class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return nums
        if len(nums) == 2:
            return nums.reverse()
        
        toChangeIndex = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                toChangeIndex = i
                break
        print("16", toChangeIndex)
        if toChangeIndex < 0:
            nums.reverse()
            return nums
        minLargerIndex = -1
        for i in range(toChangeIndex + 1, len(nums)):
            if nums[i] <= nums[toChangeIndex]:
                minLargerIndex = i - 1
                break
        if minLargerIndex < 0:
            minLargerIndex = len(nums) - 1
        print(minLargerIndex)
        nums[toChangeIndex], nums[minLargerIndex] = nums[minLargerIndex], nums[toChangeIndex]
        self.reverse(nums, toChangeIndex + 1)
        return nums
    
    def reverse(self, nums, startIndex):
        i, j = startIndex, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
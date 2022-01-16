class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i, val in enumerate(nums):
            if left == right - val:
                return i
            else:
                left += val
                right -= val
        return -1
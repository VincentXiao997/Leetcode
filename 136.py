class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numSet = set(nums)
        single = 2 * sum(numSet) - sum(nums)
        return single
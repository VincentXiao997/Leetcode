class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curMin = 1
        curSum = 0
        for num in nums:
            curSum += num
            if curSum < 0 and -curSum + 1 > curMin:
                curMin = -curSum + 1
        return curMin
        
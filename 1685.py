class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        leftSum, rightSum = 0, sum(nums)
        result = []
        length = len(nums)
        for i in range(length):
            result.append(i * nums[i] - leftSum + (rightSum - nums[i]) - (length - i - 1) * nums[i])
            leftSum += nums[i]
            rightSum -= nums[i]
        return result
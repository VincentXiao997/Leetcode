class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        preSum = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            preSum[i] = preSum[i-1] + nums[i-1]
        for i in range(1, len(nums) + 1):
            if preSum[i] == preSum[-1] - preSum[i - 1]:
                return i - 1
        return -1
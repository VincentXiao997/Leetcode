#  dp, cannot pass since it is O(n^2)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        length = len(nums)
        dp = [False for _ in range(length)]
        dp[0] = True
        for i in range(1, length):
            for j in range(i):
                if dp[j] and nums[j] + j >= i:
                    dp[i] = True
                    break
        return dp[length - 1]

# greedy, O(n)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        # length = len(nums)
        # dp = [False for _ in range(length)]
        # dp[0] = True
        # for i in range(1, length):
        #     for j in range(i):
        #         if dp[j] and nums[j] + j >= i:
        #             dp[i] = True
        #             break
        # return dp[length - 1]
        farest = 0
        for i in range(len(nums)):
            if i > farest:
                return False
            elif i + nums[i] > farest:
                farest = i + nums[i]
        return True
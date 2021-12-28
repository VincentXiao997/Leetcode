class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            operations = self.calOperations(nums, mid)
            if operations <= maxOperations:
                right = mid
            else:
                left = mid
        operations = self.calOperations(nums, left)
        if operations <= maxOperations:
            return left
        else:
            return right
        
        
    def calOperations(self, nums, k):
        counter = 0
        for num in nums:
            counter += (num - 1) // k
                # if num % k != 0:
                    # counter += 1
        return counter
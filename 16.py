class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closetSum = math.inf
        for i in range(len(nums)):
            left, right = i+1, len(nums) - 1
            while left < right:
                val = nums[left] + nums[right] + nums[i]
                if val == target:
                    return target
                if abs(target - val) < abs(closetSum - target):
                    closetSum = val
                if val > target:
                    right -= 1
                else:
                    left += 1
        return closetSum
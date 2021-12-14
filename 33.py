class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            print(left, mid, right)
            if nums[mid] == target:
                return mid
            elif nums[left] < nums[right]:
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid
            else: 
                if target <= nums[right]: # target on right
                    if nums[mid] <= nums[right]: # mid on right
                        if nums[mid] > target:
                            right = mid
                        else:
                            left = mid
                    else: # mid on left
                        left = mid
                else: # target on left
                    if nums[mid] <= nums[right]:
                        right = mid
                    else: # mid on left
                        if nums[mid] > target:
                            right = mid
                        else:
                            left = mid
                        
                    
                        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
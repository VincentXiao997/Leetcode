class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}
        self.length = len(nums)
        self.counter = 0
        for i in range(len(nums)):
            # print(i, nums[i], self.nums)
            if nums[i] != 0:
                self.nums[i] = nums[i]
                self.counter += 1
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if self.counter > vec.counter:
            return self.calculator(vec.nums, self.nums)
        else:
            return self.calculator(self.nums, vec.nums)
    
    def calculator(self, nums1, nums2):
        print(nums1, nums2)
        result = 0
        for i in nums1:
            if i in nums2:
                result += (nums1[i] * nums2[i])
        return result
            

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
class Solution:
    # bit shift
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        movement = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            movement += 1
        return left << movement
    
    # Brian Kernighan's Algorithm
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right - 1)
        return left & right
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        right = 1
        while right ** 2 < x:
            right *= 2
        left = right // 2
        while left + 1 < right:
            mid = (left + right) // 2
            power = mid ** 2
            if power == x:
                return mid
            elif power > x:
                right = mid
            else:
                left = mid
        if right ** 2 <= x:
            return right
        else:
            return left
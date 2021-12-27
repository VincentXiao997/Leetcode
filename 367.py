class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        right = 1
        while right * right < num:
            right *= 2
        left = right // 2
        while left + 1 < right:
            mid = (left + right) // 2
            sq = mid ** 2
            if sq == num:
                return True
            elif sq > num:
                right = mid
            else:
                left = mid
        if right ** 2 == num or left ** 2 == num:
            return True
        else:
            return False
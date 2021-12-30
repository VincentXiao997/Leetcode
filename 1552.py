class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        left, right = 1, max(position) - min(position)
        position.sort()
        while left + 1 < right:
            mid = (left + right) // 2
            feasible = self.hasEnoughPlace(position, m, mid)
            # print(mid, feasible)
            if feasible:
                left = mid
            else:
                right = mid
        feasible = self.hasEnoughPlace(position, m, right)
        if feasible:
            return right
        else:
            return left
        
    def hasEnoughPlace(self, position, m, minForce):
        left = None
        m -= 1
        for p in position:
            if not left :
                left = p
            else:
                if abs(p - left) >= minForce:
                    m -= 1
                    left = p
        if m > 0:
            return False
        else:
            return True
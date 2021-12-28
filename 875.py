class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left + 1 < right:
            mid = (left + right) // 2
            neededHours = self.calHours(piles, mid)
            # print(mid, neededHours)
            if neededHours == h:
                right = mid
            elif neededHours > h:
                left = mid
            else:
                right = mid
        neededHours = self.calHours(piles, left)
        if neededHours <= h:
            return left
        else:
            return right
        
    def calHours(self, piles, k):
        h = 0
        for pile in piles:
            h += math.ceil(pile / k)
        return h
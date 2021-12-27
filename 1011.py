class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left, right = max(weights), sum(weights)
        while left + 1 < right:
            mid = (left + right) // 2
            neededDays = self.toDays(weights, mid)
            if neededDays < days:
                right = mid
            elif neededDays > days:
                left = mid
            else:
                right = mid
        neededDays = self.toDays(weights, left)
        if neededDays <= days:
            return left
        else:
            return right
    
    def toDays(self, weights, capacity):
        days = 0
        curW = 0
        for w in weights:
            if curW + w > capacity:
                days += 1
                curW = w
            else:
                curW += w
        return days + 1
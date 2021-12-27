class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 1:
            return 0
        
        ith = 1
        while self.getTotalNum(ith) < n:
            ith *= 2
        
        left, right = ith // 2, ith
        while left + 1 < right:
            mid = (left + right) // 2
            num = self.getTotalNum(mid)    
            if num > n:
                right = mid
            elif num < n:
                left = mid
            else:
                return mid
        num = self.getTotalNum(right)
        if num <= n:
            return right
        else:
            return left
        
            
            
            
    def getTotalNum(self, ith):
        return (1 + ith) * ith // 2
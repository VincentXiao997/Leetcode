class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        minDays = m * k
        if len(bloomDay) < minDays:
            return -1
        left, right = minDays, max(bloomDay)
        while left + 1 < right:
            mid = (left + right) // 2
            numOfBouquets = self.calNumOfBouquets(bloomDay, k, mid)
            if numOfBouquets > m:
                right = mid
            elif numOfBouquets < m:
                left = mid
            else:
                right  = mid
        numOfBouquets = self.calNumOfBouquets(bloomDay, k, left)
        if numOfBouquets >= m:
            return left
        else:
            return right
        
    def calNumOfBouquets(self, bloomDay, k, d):
        adjacentNum = 0
        numOfBouquets = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= d:
                adjacentNum += 1
                if adjacentNum >= k:
                    numOfBouquets += 1
                    adjacentNum = 0
            else:
                adjacentNum = 0
        return numOfBouquets
                    

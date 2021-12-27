class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.memo_search(triangle, 0, 0, {})
    
    def memo_search(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0
        elif (x, y) in memo:
            return memo[(x, y)]
        
        left = self.memo_search(triangle, x + 1, y, memo)
        right = self.memo_search(triangle, x + 1, y + 1, memo)
        
        result = min(left, right) + triangle[x][y]
        memo[(x, y)] = result
        return result
        
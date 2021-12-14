# memory search
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dfs(0, n, {})
    
    def dfs(self, i, n, memo):
        if n == i:
            return 1
        if n < i:
            return 0
        if i in memo:
            return memo[i]
        result = self.dfs(i + 1, n, memo) + self.dfs(i+2, n, memo)
        memo[i] = result
        return result

# dp
class Solution:
    def climbStairs(self, n: int) -> int:
        distanceMap = [0 for _ in range(n + 1)]
        distanceMap[0] = distanceMap[1] = 1
        for i in range(2, n + 1):
            distanceMap[i] = distanceMap[i-1] + distanceMap[i-2]
        return distanceMap[-1]
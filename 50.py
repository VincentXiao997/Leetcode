class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.helper(x, -n)
        else:
            return self.helper(x, n)
        
    def helper(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        result = self.helper(x, n//2)
        if n % 2 == 0:
            return result * result
        else:
            return result * result * x
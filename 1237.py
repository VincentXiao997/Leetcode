"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

# binary Search
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        x = 1
        while customfunction.f(x, 1) <= z and x < 1001:
            left, right = 1, 1000
            while left + 1 < right:
                mid = (left + right) // 2
                val = customfunction.f(x, mid)
                if val == z:
                    result.append([x, mid])
                    break
                elif val > z:
                    right = mid
                else:
                    left = mid
            if customfunction.f(x, left) == z:
                result.append([x, left])
            elif customfunction.f(x, right) == z:
                result.append([x, right])
            x += 1
        return result


# two pointers
class Solution2:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        x = 1
        y = 1000
        while x < 1001 and y > 0:
            while y > 1 and customfunction.f(x, y) > z:
                y -= 1
            if customfunction.f(x, y) == z:
                result.append([x, y])
            x += 1
        return result
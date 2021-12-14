class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i in range(len(heights)):
            if len(stack) == 0:
                stack.append(i)
            elif heights[i] >= heights[stack[-1]]:
                while stack:
                    if heights[stack[-1]] <= heights[i]:
                        stack.pop()
                    else:
                        break
                stack.append(i)
            else:
                stack.append(i)
        return stack
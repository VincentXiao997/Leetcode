class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        result = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if len(stack) < 1:
                    result += 1
                else:
                    stack.pop()
        result += len(stack)
        return result
                
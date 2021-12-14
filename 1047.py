class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return s
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            else:
                lastChar = stack.pop()
                if lastChar != s[i]:
                    stack.append(lastChar)
                    stack.append(s[i])
        result = "".join(stack)
        return result
                
            
        
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        toDeleteIndexs = []
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) > 0:
                    stack.pop()
                else:
                    toDeleteIndexs.append(i)
        toDeleteIndexs += stack
        result = ""
        for i in range(len(s)):
            if i in toDeleteIndexs:
                continue
            else:
                result += s[i]
        return result
        
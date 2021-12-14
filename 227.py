class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i+=1
                continue
            if s[i] == "+" or s[i] == "-":
                stack.append(s[i])
                i += 1
            elif s[i] == "*" or s[i] == "/":
                operator = s[i]
                leftNum = int(stack.pop())
                i += 1
                rightStr = ""
                while i < len(s):
                    if s[i].isdigit():
                        rightStr += s[i]
                        i += 1
                    elif s[i] == " ":
                        i+=1
                        continue
                    else:
                        break
                if operator == "*":
                    stack.append(leftNum * int(rightStr))
                else:
                    stack.append(leftNum // int(rightStr))
            else:
                numStr = ""
                while i < len(s):
                    if s[i].isdigit():
                        numStr += s[i]
                        i += 1
                    elif s[i] == " ":
                        i+=1
                        continue
                    else:
                        break
                stack.append(numStr)
        # print(stack)
        stack = collections.deque(stack)
        leftNum = int(stack.popleft())
        while stack:
            # print(stack)
            operator = stack.popleft()
            rightNum = int(stack.popleft())
            # print(operato/r, rightNum)
            if operator == "+":
                leftNum = leftNum + rightNum
            else:
                leftNum = leftNum - rightNum
        return leftNum
                
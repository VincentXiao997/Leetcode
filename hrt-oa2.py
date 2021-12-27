def solution(s):
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        else:
            if c == "A":
                if stack[-1] == "B":
                    stack.pop()
                else:
                    stack.append(c)
            elif c == "B":
                if stack[-1] == "A":
                    stack.pop()
                else:
                    stack.append(c)
            elif c == "C":
                if stack[-1] == "D":
                    stack.pop()
                else:
                    stack.append(c)
            elif c == "D":
                if stack[-1] == "C":
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
    return "".join(stack)

print(solution(""))
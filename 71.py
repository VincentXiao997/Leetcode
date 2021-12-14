class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        # for i in range(len(path)):
        while i < len(path):
            print(i, stack)
            if path[i] == "/":
                while i + 1 < len(path) and path[i+1] == "/":
                    i += 1
                stack.append("/")
            elif path[i] == ".":
                currentS = "."
                while i + 1 < len(path) and path[i+1] != "/":
                    currentS += path[i+1]
                    i += 1
                if currentS == ".":
                    stack.pop()
                elif currentS == "..":
                    stack.pop()
                    if stack:
                        stack.pop()
                        stack.pop()
                else:
                    stack.append(currentS)
            else:
                s = path[i]
                while i+1 < len(path) and path[i+1] != "/":
                    s += path[i+1]
                    i += 1
                stack.append(s)
            i+=1
        if len(stack) > 1:
            lastS = stack.pop()
            if lastS != "/":
                stack.append(lastS)
        elif not stack:
            return "/"
        return "".join(stack)
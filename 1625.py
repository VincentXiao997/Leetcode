class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set([s])
        queue = collections.deque([s])
        minS = s
        while queue:
            # print(queue)
            curS = queue.popleft()
            newS1 = self.add(curS, a)
            newS2 = self.rotate(curS, b)
            # print(newS1, newS2)
            if newS1 not in seen:
                seen.add(newS1)
                queue.append(newS1)
            if newS2 not in seen:
                seen.add(newS2)
                queue.append(newS2)
            if newS1 < minS:
                minS = newS1
            if newS2 < minS:
                minS = newS2
        return minS
        
    
    
    def add(self, s, a):
        for i in range(len(s) - 1, -1, -2):
            num = int(s[i])
            # print(num)
            num = (num + a) % 10
            # print(num)
            s = s[:i] + str(num) + s[i+1:]
        return s
        
    def rotate(self, s, b):
        return s[b:] + s[:b]
    
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        hashSet = {}
        for start, end, inc in updates:
            if start in hashSet:
                hashSet[start] += inc
            else:
                hashSet[start] = inc
            if end + 1 < length:
                if end + 1 in hashSet:
                    hashSet[end + 1] -= inc
                else:
                    hashSet[end + 1] = -inc
        results = []
        curVal = 0
        for i in range(length):
            if i in hashSet:
                curVal += hashSet[i]
            results.append(curVal)
        return results
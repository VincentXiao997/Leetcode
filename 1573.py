class Solution:
    def numWays(self, s: str) -> int:
        modulo = 10**9 + 7
        indexs = {}
        counter = 0
        result = 0
        for i,c in enumerate(s):
            if c == "1":
                counter += 1
                indexs[counter] = i
        if counter == 0:
            return (len(s)-2+1)*(len(s)-2)//2%modulo
        elif counter % 3 != 0 or counter < 3:
            return result
        firstIndex = indexs[counter // 3]
        secondIndex = indexs[counter // 3 * 2]
        firstNext = indexs[counter//3+1]
        secondNext = indexs[counter // 3 * 2 + 1]
        return (firstNext - firstIndex)*(secondNext - secondIndex)%modulo
        
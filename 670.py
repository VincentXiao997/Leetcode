class Solution:
    def maximumSwap(self, num: int) -> int:
        if not num:
            return num
        numStr = list(str(num))
        maxVal = -math.inf
        maxIndex = None
        canSwap = None
        for i in range(len(numStr)-1, -1, -1):
            if int(numStr[i]) > maxVal:
                maxVal = int(numStr[i])
                maxIndex = i
            elif int(numStr[i]) < maxVal:
                canSwap = [i, maxIndex]
        if not canSwap:
            return num
        numStr[canSwap[0]], numStr[canSwap[1]] =  numStr[canSwap[1]], numStr[canSwap[0]]
        return int("".join(numStr))
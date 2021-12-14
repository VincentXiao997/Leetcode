class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        xList = []
        yList = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    xList.append(x)
                    yList.append(y)
        yList.sort()
        xMid = xList[len(xList) // 2]
        yMid = yList[len(yList) // 2]
        return self.calculateDistance(xMid, xList) + self.calculateDistance(yMid, yList)
    
    def calculateDistance(self, mid, List):
        distance = 0
        for x in List:
            distance += abs(mid - x)
        return distance
        
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        map = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for x in range(len(obstacleGrid)):
            if obstacleGrid[x][0] == 1:
                break
            map[x][0] = 1
        for y in range(len(obstacleGrid[0])):
            if  obstacleGrid[0][y] == 1:
                break
            map[0][y] = 1
        for x in range(1, len(obstacleGrid)):
            for y in range(1, len(obstacleGrid[x])):
                if obstacleGrid[x][y] == 1:
                    continue
                else:
                    map[x][y] = map[x-1][y] + map[x][y-1]
        return map[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
        
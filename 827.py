class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        islandSizes = {}
        index = 2
        visited = [[False for _ in range(len(grid))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j]:
                    visited[i][j] = True
                    if grid[i][j] == 1:
                        islandSizes[index] = self.dfs(grid, i, j, visited, index)
                        index += 1
        visited = [[False for _ in range(len(grid))] for _ in range(len(grid))]
        maxSize = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0 and not visited[i][j]:
                    visited[i][j] = True
                    upIndex, downIndex, leftIndex, rightIndex = 0,0,0,0
                    sumSize = 0
                    neighborIslands = []
                    if i-1 >= 0 and grid[i-1][j] != 0:
                        upIndex = grid[i-1][j]
                        neighborIslands.append(upIndex)
                        sumSize += islandSizes[upIndex]
                    if i+1 < len(grid) and grid[i+1][j] != 0:
                        downIndex = grid[i+1][j]
                        if downIndex not in neighborIslands:
                            neighborIslands.append(downIndex)
                            sumSize += islandSizes[downIndex]
                    if j-1 >= 0 and grid[i][j-1] != 0:
                        leftIndex = grid[i][j-1]
                        if leftIndex not in neighborIslands:
                            neighborIslands.append(leftIndex)
                            sumSize += islandSizes[leftIndex]
                    if j+1 < len(grid) and grid[i][j+1] != 0:
                        rightIndex = grid[i][j+1]
                        if rightIndex not in neighborIslands:
                            neighborIslands.append(rightIndex)
                            sumSize += islandSizes[rightIndex]
                    if sumSize + 1 > maxSize:
                        maxSize = sumSize + 1
        if maxSize == 0:
            maxSize = max(list(islandSizes.values()))
        return maxSize
                    
        
    
    def dfs(self, grid, i, j, visited, index):
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        if grid[i][j] == 0:
            return 0
        grid[i][j] = index
        values = []
        for direct in directions:
            newi = i + direct[0]
            newj = j + direct[1]
            if newi < len(grid) and newi >= 0 and newj < len(grid) and newj >= 0:
                if not visited[newi][newj]:
                    visited[newi][newj] = False
                    if grid[newi][newj] == 1:
                        values.append(self.dfs(grid, newi, newj, visited, index))
        return sum(values) + 1
        
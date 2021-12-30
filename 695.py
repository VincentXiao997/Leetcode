class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowSize, colSize = len(grid), len(grid[0])
        visited = [[False for _ in range(colSize)] for _ in range(rowSize)]
        maxArea = 0
        for x in range(rowSize):
            for y in range(colSize):
                if grid[x][y] == 1:
                    if not visited[x][y]:
                        visited[x][y] = True
                        curArea = self.checkArea(grid, visited, x, y, rowSize, colSize)
                        if curArea > maxArea:
                            maxArea = curArea
        return maxArea
        
        
        
        
    def checkArea(self, grid, visited, x, y, rowSize, colSize):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = collections.deque([(x, y)])
        area = 0
        visited[x][y] = True
        while queue:
            curX, curY = queue.popleft()
            area += 1
            for dirX, dirY in directions:
                newX, newY = curX + dirX, curY + dirY
                if newX >= 0 and newX < rowSize and newY >= 0 and newY < colSize:
                    if not visited[newX][newY] and grid[newX][newY] == 1:
                        visited[newX][newY] = True
                        queue.append((newX, newY))
        return area
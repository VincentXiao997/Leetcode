import math
import heapq

# binary search              
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[n - 1][n - 1]
        
        while left < right:
            mid = (left + right) // 2
            numOfSmaller, smaller, larger = self.helper(matrix, mid)
            if numOfSmaller == k:
                return smaller
            elif numOfSmaller < k:
                left = larger
            else:
                right = smaller
        return left
            
    def helper(self, matrix, k):
        n = len(matrix)
        i, j = len(matrix) - 1, 0
        counter = 0
        smallerThanK = -math.inf
        largerThanK = math.inf
        while i >= 0 and j < n:
            while i >= 0 and matrix[i][j] > k:
                if matrix[i][j] < largerThanK:
                    largerThanK = matrix[i][j]
                i -= 1
            if i >= 0:
                if smallerThanK < matrix[i][j]:
                    smallerThanK = matrix[i][j]
                counter += (i + 1)
                j += 1
        return counter, smallerThanK, largerThanK



# heap
class Solution_Heap:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        for i in range(len(matrix)):
            heap.append((matrix[i][0], i, 0))
        heapq.heapify(heap)
        counter = 0
        while counter < k - 1:
            _, row, col = heapq.heappop(heap)
            counter += 1
            if col + 1 < n:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
        val, _, _ = heapq.heappop(heap)
        return val
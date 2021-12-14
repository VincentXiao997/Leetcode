# class Solution:
    
#     def countLessEqual(self, matrix, mid, smaller, larger):
        
#         count, n = 0, len(matrix)
#         row, col = n - 1, 0
        
#         while row >= 0 and col < n:
#             if matrix[row][col] > mid:
               
#                 # As matrix[row][col] is bigger than the mid, let's keep track of the
#                 # smallest number greater than the mid
#                 larger = min(larger, matrix[row][col])
#                 row -= 1
                
#             else:
                
#                 # As matrix[row][col] is less than or equal to the mid, let's keep track of the
#                 # biggest number less than or equal to the mid
                
#                 smaller = max(smaller, matrix[row][col])
#                 count += row + 1
#                 col += 1

#         return count, smaller, larger
    
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
#         n = len(matrix)
#         start, end = matrix[0][0], matrix[n - 1][n - 1]
#         while start < end:
#             mid = start + (end - start) / 2
#             smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

#             count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger)

#             if count == k:
#                 return smaller
#             if count < k:
#                 start = larger  # search higher
#             else:
#                 end = smaller  # search lower

#         return start

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]
        smaller, greater = matrix[0][0], matrix[n-1][n-1]
        while left < right:
            mid = (left + right) / 2
            smaller, greater = matrix[0][0], matrix[n-1][n-1]
            leftHandSideNums, smaller, greater = self.leftHandSideNums(matrix, mid, smaller, greater)
            if leftHandSideNums == k:
                return smaller
            if leftHandSideNums < k:
                left = greater
            else:
                right = smaller
        return left
        
    def leftHandSideNums(self, matrix, val, smaller, greater):
        length = len(matrix)
        x, y = length - 1, 0
        result = 0
        while x >= 0 and y < length:
            if matrix[x][y] > val:
                greater = min(matrix[x][y], greater)
                x -= 1
            else:
                smaller = max(smaller, matrix[x][y])
                result += (x+1)
                y += 1
        return result, smaller, greater
            
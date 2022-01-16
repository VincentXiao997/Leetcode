class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        if not mat:
            return [[]]
        h, w = len(mat), len(mat[0])
        preSum = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
        results = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                preSum[i][j] = preSum[i-1][j] + preSum[i][j - 1] - preSum[i-1][j-1] + mat[i - 1][j - 1]
        for i in range(h):
            for j in range(w):
                lowI = i - k if i - k >= 0 else 0
                highI = i + 1 + k if i + 1 + k <= h else h
                lowJ = j - k if j - k >= 0 else 0
                highJ = j + 1 + k if j + 1 + k <= w else w
                results[i][j] = preSum[highI][highJ] - preSum[highI][lowJ] - preSum[lowI][highJ] + preSum[lowI][lowJ]
        return results
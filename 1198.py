class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        if not mat:
            return -1
        for num in mat[0]:
            findAll = True
            for i in range(1, len(mat)):
                if not self.binarySearch(mat[i], num):
                    findAll = False
                    break
            if findAll:
                return num
        return -1
                
    def binarySearch(self, arr, target):
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                right = mid
            else:
                left = mid
        if arr[left] == target or arr[right] == target:
            return True
        else:
            return False
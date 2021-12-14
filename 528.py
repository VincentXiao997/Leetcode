class Solution:

    def __init__(self, w: List[int]):
        weightList = [0]
        for i in range(len(w)-1):
            weightList.append(weightList[-1] + w[i])
        self.weightList = weightList
        self.max = weightList[-1] + w[-1]
        
    def pickIndex(self) -> int:
        selection = random.random() * self.max
        return self.binarySearch(selection)

    def binarySearch(self, val):
        left, right = 0, len(self.weightList) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.weightList[mid] == val:
                return mid
            elif self.weightList[mid] > val:
                right = mid
            else:
                left = mid
        if self.weightList[right] < val:
            return right
        else:
            return left
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
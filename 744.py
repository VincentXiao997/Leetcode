class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        
        left, right = 0, len(letters) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            elif letters[mid] < target:
                left = mid
            else:
                left = mid
        if letters[left] > target:
            return letters[left]
        else:
            return letters[right]
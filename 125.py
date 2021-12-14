class Solution:
    def isPalindrome(self, s: str) -> bool:
        filted = ""
        
        for c in s:
            if c.isalpha():
                filted += c.lower()
            elif c.isnumeric():
                filted += c
        left, right = 0, len(filted) - 1
        while left < right:
            if filted[left] != filted[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
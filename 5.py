class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        longest = 0
        longestL, longestR = 0, 0
        # for odd
        for i in range(len(s)):
            left, right = self.find_palindrome(s, i, i)
            if right - left + 1 > longest:
                longest = right - left + 1
                longestL = left
                longestR = right

        # for even
        for i in range(len(s) - 1):
            left, right = self.find_palindrome(s, i, i + 1)
            if right - left + 1 > longest:
                longest = right - left + 1
                longestL = left
                longestR = right
        return s[longestL: longestR+1]


    def find_palindrome(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        return left + 1, right - 1
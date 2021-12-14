# two pointers

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        option1, option2 = None, None
        while left <right:
            if s[left] != s[right]:
                option1 = s[:left] + s[left+1:]
                option2 = s[:right] + s[right+1:]
                break
            else:
                left += 1 
                right -= 1
        if option1 and option2:
            option1Result = self.checkPalindrome(option1)
            option2Result = self.checkPalindrome(option2)
        else:
            option1Result = option2Result = True
        return option1Result or option2Result
    def checkPalindrome(self, s: str):
        print(s)
        left, right = 0, len(s) - 1
        while left <right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True


# class Solution:
#     def validPalindrome(self, s: str) -> bool:
        
#         if s == s[::-1]: return True
        
#         for i in range(len(s)//2):
            
#             if s[i] != s[len(s)-1-i]: 
                
#                 s_copy = s[:i] + s[i+1:]
#                 if s_copy == s_copy[::-1]: return True
                
#                 s_copy = s[:len(s)-1-i] + s[len(s)-i:]
#                 if s_copy == s_copy[::-1]: return True
                
#                 return False
                
#         return True
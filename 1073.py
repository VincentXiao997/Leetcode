class Solution:
    def addNegabinary(self, arr1, arr2):
        print(self.negabinaryToDecimal(arr1))

        print(self.negabinaryToDecimal(arr2))
        return self.decimalToNegabinary(self.negabinaryToDecimal(arr1) + self.negabinaryToDecimal(arr2))
        
    def negabinaryToDecimal(self, arr):
        # arr.reverse()
        result = 0
        i = 1
        for n in arr:
            result += i * n
            i *= -2
        return result
    
    def decimalToNegabinary(self, num):
        if num == 0:
            return [0]
        result = []
        while num:
            r = num % -2
            if r:
                num -= 1
            num //= -2
            result.append(abs(r))
        # result.reverse()
        return result

solution = Solution()
print(solution.addNegabinary([0,1,1,0,0,1,0,1,1,1,0,1,0,1,1], [0,0,1,0,0,1,1,1,1,1,0,1]))
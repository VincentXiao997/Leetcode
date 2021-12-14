class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        len1, len2 = len(num1) - 1, len(num2) - 1
        addOne = False
        result = ""
        for i in range(0, len(num1)):
            if len2 - i < 0:
                if addOne:
                    newInt = int(num1[len1 - i]) + 1
                    if newInt > 9:
                        newInt %= 10
                        addOne = True
                    else:
                        addOne = False
                    result = str(newInt) + result
                else:
                    addOne = False
                    result = num1[len1 - i] + result
                continue
            
            if addOne:
                newInt = int(num1[len1 - i]) + int(num2[len2 - i]) + 1
                if newInt > 9:
                    newInt %= 10
                    addOne = True
                else:
                    addOne = False
                result = str(newInt) + result
            else:
                newInt = int(num1[len1 - i]) + int(num2[len2 - i])
                if newInt > 9:
                    newInt %= 10
                    addOne = True
                else:
                    addOne = False
                result = str(newInt) + result
        if addOne:
            result = "1" + result
        return result
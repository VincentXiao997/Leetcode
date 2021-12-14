class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        result = []
        while n:
            r = n % -2
            if r:
                n -= 1
            n = n // -2
            result.append(str(abs(r)))
        result.reverse()
        return "".join(result)
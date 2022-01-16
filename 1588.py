class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        sums = [0 for _ in range(n + 1)]
        sums[0] = 0
        for i in range(1, n + 1):
            sums[i] = sums[i-1] + arr[i - 1]
        length = 1
        result = 0
        while length <= n:
            left = 0
            while left + length <= n:
                result += sums[left + length] - sums[left] 
                left += 1
            length += 2
        return result
            
                
                
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left + 1 < right:
            mid = (left + right) // 2
            isBad = isBadVersion(mid)
            if isBad:
                right = mid
            else:
                left = mid
        isBad = isBadVersion(left)
        if isBad:
            return left
        else:
            return right
        
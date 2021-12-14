class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        write, read1, read2 = m+n-1, m-1, n-1
        while read1 >= 0 or read2 >= 0:      
            if read1 < 0:
                nums1[write] = nums2[read2]
                write -= 1
                read2 -= 1
            elif read2 < 0:
                nums1[write] = nums1[read1]
                write -= 1
                read1 -= 1
            elif nums1[read1] >= nums2[read2]:
                nums1[write] = nums1[read1]
                write -= 1
                read1 -= 1
            else:
                nums1[write] = nums2[read2]
                write -= 1
                read2 -= 1
               
from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        result = []

        for num in c1:
            if num in c2:
                result.extend([num] * min(c1[num], c2[num]))

        return result
    
# 1ST JULY, 2025, TUESDAY, 10:01 PM

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        return list(set(nums1) & set(nums2))
        



# 1ST JULY, 2025, TUESDAY, 10:18 PM

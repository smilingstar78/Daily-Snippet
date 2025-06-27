class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.nums = nums
        for i in range(1,len(self.nums)):
            nums[i] = nums[i]+nums[i-1]
            # print(nums[i])
        return nums

# 27th June, 2025, Friday, 10:30pm

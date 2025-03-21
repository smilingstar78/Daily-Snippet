class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]  # returning indexes directly

# Example driver code:
sol = Solution()
print(sol.twoSum([2, 6, 3, 1, 5], 7))  # Output: [0, 1]

#21st March, 2025, Friday, 21st Ramadan, 10:29pm

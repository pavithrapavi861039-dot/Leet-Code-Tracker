# Last updated: 7/18/2026, 9:34:23 PM
1class Solution:
2    def pivotIndex(self, nums):
3        total = sum(nums)
4        left_sum = 0
5        for i in range(len(nums)):
6            if left_sum == total - left_sum - nums[i]:
7                return i
8            left_sum += nums[i]
9        return -1
10        
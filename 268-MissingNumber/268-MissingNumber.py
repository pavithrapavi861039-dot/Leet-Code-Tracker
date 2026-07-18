# Last updated: 7/18/2026, 9:18:03 PM
1class Solution:
2    def missingNumber(self, nums):
3        n = len(nums)
4        return n * (n + 1) // 2 - sum(nums)
5        
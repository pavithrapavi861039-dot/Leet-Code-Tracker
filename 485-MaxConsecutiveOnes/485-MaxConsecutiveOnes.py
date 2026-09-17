# Last updated: 9/17/2026, 10:22:23 AM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums):
3        count = 0
4        maximum = 0
5        for num in nums:
6            if num == 1:
7                count += 1
8                maximum = max(maximum, count)
9            else:
10                count = 0
11        return maximum
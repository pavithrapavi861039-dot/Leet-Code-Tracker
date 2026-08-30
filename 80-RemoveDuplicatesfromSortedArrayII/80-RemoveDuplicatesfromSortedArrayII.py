# Last updated: 8/30/2026, 1:49:48 PM
1class Solution:
2    def removeDuplicates(self, nums):
3        k = 0
4
5        for num in nums:
6            if k < 2 or num != nums[k - 2]:
7                nums[k] = num
8                k += 1
9
10        return k
11        
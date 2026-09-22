# Last updated: 9/22/2026, 9:21:14 AM
1class Solution:
2    def minPatches(self, nums, n):
3        miss = 1
4        i = 0
5        patches = 0
6
7        while miss <= n:
8            if i < len(nums) and nums[i] <= miss:
9                miss += nums[i]
10                i += 1
11            else:
12                miss += miss
13                patches += 1
14
15        return patches
16        
# Last updated: 7/18/2026, 9:20:56 PM
1class Solution:
2    def maxProduct(self, nums):
3        cur_max = cur_min = result = nums[0]
4        for i in range(1, len(nums)):
5            x = nums[i]
6            if x < 0:
7                cur_max, cur_min = cur_min, cur_max   
8            cur_max = max(x, cur_max * x)
9            cur_min = min(x, cur_min * x)  
10            result = max(result, cur_max)
11        return result
# Last updated: 7/18/2026, 9:32:50 PM
1class Solution:
2    def maxSubarraySumCircular(self, nums):
3        total_sum = 0
4        cur_max = cur_min = 0
5        max_sum = nums[0]
6        min_sum = nums[0]
7        for num in nums:
8            cur_max = max(num, cur_max + num)
9            max_sum = max(max_sum, cur_max)
10            cur_min = min(num, cur_min + num)
11            min_sum = min(min_sum, cur_min)
12            total_sum += num
13        if max_sum < 0:
14            return max_sum
15        return max(max_sum, total_sum - min_sum)
16        
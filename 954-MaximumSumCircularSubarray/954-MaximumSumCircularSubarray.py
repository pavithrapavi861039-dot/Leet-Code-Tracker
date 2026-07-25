# Last updated: 7/25/2026, 9:27:03 AM
class Solution:
    def maxSubarraySumCircular(self, nums):
        total_sum = 0
        cur_max = cur_min = 0
        max_sum = nums[0]
        min_sum = nums[0]
        for num in nums:
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)
            total_sum += num
        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)
        
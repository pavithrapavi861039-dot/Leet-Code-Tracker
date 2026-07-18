# Last updated: 7/18/2026, 9:24:50 PM
1class Solution:
2    def subarraySum(self, nums, k):
3        count = 0
4        prefix_sum = 0
5        hashmap = {0: 1}
6        for num in nums:
7            prefix_sum += num
8            if prefix_sum - k in hashmap:
9                count += hashmap[prefix_sum - k]
10            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
11        return count
12        
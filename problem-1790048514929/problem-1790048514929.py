# Last updated: 9/22/2026, 9:11:54 AM
1class Solution:
2    def numberOfArithmeticSlices(self, nums):
3        n = len(nums)
4        dp = [dict() for _ in range(n)]
5        ans = 0
6
7        for i in range(n):
8            for j in range(i):
9                diff = nums[i] - nums[j]
10
11                count = dp[j].get(diff, 0)
12
13                dp[i][diff] = dp[i].get(diff, 0) + count + 1
14
15                ans += count
16
17        return ans
18        
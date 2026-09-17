# Last updated: 9/17/2026, 9:54:13 AM
1class Solution:
2    def splitArray(self, nums, k):
3        left = max(nums)
4        right = sum(nums)
5
6        while left < right:
7            mid = (left + right) // 2
8            parts = 1
9            current = 0
10
11            for num in nums:
12                if current + num > mid:
13                    parts += 1
14                    current = num
15                else:
16                    current += num
17
18            if parts <= k:
19                right = mid
20            else:
21                left = mid + 1
22
23        return left
24        
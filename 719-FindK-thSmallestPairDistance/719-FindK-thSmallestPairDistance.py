# Last updated: 7/25/2026, 9:55:51 AM
1class Solution:
2    def smallestDistancePair(self, nums, k):
3        nums.sort()
4        def count(mid):
5            cnt = 0
6            left = 0
7            for right in range(len(nums)):
8                while nums[right] - nums[left] > mid:
9                    left += 1
10                cnt += right - left
11            return cnt
12        left, right = 0, nums[-1] - nums[0]
13        while left < right:
14            mid = (left + right) // 2 
15            if count(mid) < k:
16                left = mid + 1
17            else:
18                right = mid
19        return left
20        
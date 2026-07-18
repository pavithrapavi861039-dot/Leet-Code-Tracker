# Last updated: 7/18/2026, 9:30:58 PM
1class Solution:
2    def findDuplicate(self, nums):
3        slow = nums[0]
4        fast = nums[0]
5        while True:
6            slow = nums[slow]
7            fast = nums[nums[fast]]
8            if slow == fast:
9                break
10        slow = nums[0]
11        while slow != fast:
12            slow = nums[slow]
13            fast = nums[fast]
14        return slow
# Last updated: 7/18/2026, 9:28:02 PM
1class Solution:
2    def longestConsecutive(self, nums):
3        num_set = set(nums)
4        longest = 0
5        for num in num_set:
6            if num - 1 not in num_set:
7                current = num
8                length = 1
9                while current + 1 in num_set:
10                    current += 1
11                    length += 1
12                longest = max(longest, length)
13        return longest
14        
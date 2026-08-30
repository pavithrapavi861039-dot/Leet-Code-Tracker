# Last updated: 8/30/2026, 1:48:14 PM
1class Solution:
2    def subsets(self, nums):
3        result = []
4
5        def backtrack(start, path):
6            result.append(path[:])
7
8            for i in range(start, len(nums)):
9                path.append(nums[i])
10                backtrack(i + 1, path)
11                path.pop()
12
13        backtrack(0, [])
14        return result
15        
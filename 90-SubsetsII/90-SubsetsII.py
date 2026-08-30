# Last updated: 8/30/2026, 1:43:24 PM
1class Solution:
2    def subsetsWithDup(self, nums):
3        nums.sort()
4        result = []
5
6        def backtrack(start, path):
7            result.append(path[:])
8
9            for i in range(start, len(nums)):
10                if i > start and nums[i] == nums[i - 1]:
11                    continue
12                path.append(nums[i])
13                backtrack(i + 1, path)
14                path.pop()
15
16        backtrack(0, [])
17        return result
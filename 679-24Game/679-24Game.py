# Last updated: 7/25/2026, 9:49:38 AM
1class Solution:
2    def judgePoint24(self, cards):
3        def dfs(nums):
4            if len(nums) == 1:
5                return abs(nums[0] - 24) < 1e-6
6            for i in range(len(nums)):
7                for j in range(len(nums)):
8                    if i != j:
9                        next_nums = []
10                        for k in range(len(nums)):
11                            if k != i and k != j:
12                                next_nums.append(nums[k])
13                        for val in compute(nums[i], nums[j]):
14                            next_nums.append(val)
15                            if dfs(next_nums):
16                                return True
17                            next_nums.pop()
18            return False
19        def compute(a, b):
20            res = [a + b, a - b, b - a, a * b]
21            if abs(b) > 1e-6:
22                res.append(a / b)
23            if abs(a) > 1e-6:
24                res.append(b / a)
25            return res
26        return dfs([float(x) for x in cards])
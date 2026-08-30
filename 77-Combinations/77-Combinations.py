# Last updated: 8/30/2026, 1:47:30 PM
1class Solution:
2    def combine(self, n, k):
3        result = []
4
5        def backtrack(start, path):
6            if len(path) == k:
7                result.append(path[:])
8                return
9
10            for i in range(start, n + 1):
11                path.append(i)
12                backtrack(i + 1, path)
13                path.pop()
14
15        backtrack(1, [])
16        return result
17        
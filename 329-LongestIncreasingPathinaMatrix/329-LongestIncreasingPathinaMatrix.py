# Last updated: 7/31/2026, 9:41:18 AM
1class Solution(object):
2    def longestIncreasingPath(self, matrix):
3        if not matrix or not matrix[0]:
4            return 0
5        m, n = len(matrix), len(matrix[0])
6        dp = [[0] * n for _ in range(m)]
7        directions = [(0,1), (0,-1), (1,0), (-1,0)]
8        def dfs(i, j):
9            if dp[i][j] != 0:
10                return dp[i][j]
11            max_path = 1
12            for dx, dy in directions:
13                x, y = i + dx, j + dy
14                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
15                    max_path = max(max_path, 1 + dfs(x, y))
16            dp[i][j] = max_path
17            return max_path
18        result = 0
19        for i in range(m):
20            for j in range(n):
21                result = max(result, dfs(i, j))
22        return result
23        
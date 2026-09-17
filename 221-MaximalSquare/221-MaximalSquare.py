# Last updated: 9/17/2026, 9:42:33 AM
1class Solution:
2    def maximalSquare(self, matrix):
3        m = len(matrix)
4        n = len(matrix[0])
5        dp = [[0] * (n + 1) for _ in range(m + 1)]
6        max_side = 0
7        for i in range(1, m + 1):
8            for j in range(1, n + 1):
9                if matrix[i - 1][j - 1] == "1":
10                    dp[i][j] = 1 + min(
11                        dp[i - 1][j],
12                        dp[i][j - 1],
13                        dp[i - 1][j - 1]
14                    )
15                    max_side = max(max_side, dp[i][j])
16        return max_side * max_side
17        
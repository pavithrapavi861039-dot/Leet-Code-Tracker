# Last updated: 7/25/2026, 9:31:41 AM
1class Solution:
2    def strangePrinter(self, s):
3        n = len(s)
4        dp = [[0] * n for _ in range(n)]
5        for i in range(n):
6            dp[i][i] = 1
7        for length in range(2, n + 1):
8            for i in range(n - length + 1):
9                j = i + length - 1
10                dp[i][j] = dp[i + 1][j] + 1
11                for k in range(i + 1, j + 1):
12                    if s[i] == s[k]:
13                        dp[i][j] = min(dp[i][j],
14                                       dp[i + 1][k - 1] + dp[k][j])
15        
16        return dp[0][n - 1]
17        
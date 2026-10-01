# Last updated: 10/1/2026, 9:46:20 AM
1class Solution:
2    def rearrangeSticks(self, n, k):
3        MOD = 1000000007
4
5        dp = [[0] * (k + 1) for _ in range(n + 1)]
6        dp[0][0] = 1
7
8        for i in range(1, n + 1):
9            for j in range(1, min(i, k) + 1):
10                dp[i][j] = (
11                    dp[i - 1][j - 1]
12                    + dp[i - 1][j] * (i - 1)
13                ) % MOD
14
15        return dp[n][k]
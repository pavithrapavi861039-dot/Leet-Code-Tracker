# Last updated: 9/17/2026, 10:03:40 AM
1class Solution:
2    def countPalindromicSubsequences(self, s):
3        MOD = 10**9 + 7
4        n = len(s)
5
6        dp = [[0] * n for _ in range(n)]
7
8        for i in range(n):
9            dp[i][i] = 1
10
11        for length in range(2, n + 1):
12            for i in range(n - length + 1):
13                j = i + length - 1
14
15                if s[i] == s[j]:
16                    l = i + 1
17                    r = j - 1
18
19                    while l <= r and s[l] != s[i]:
20                        l += 1
21
22                    while l <= r and s[r] != s[i]:
23                        r -= 1
24
25                    if l > r:
26                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
27                    elif l == r:
28                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
29                    else:
30                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[l + 1][r - 1]
31                else:
32                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
33
34                dp[i][j] %= MOD
35
36        return dp[0][n - 1]
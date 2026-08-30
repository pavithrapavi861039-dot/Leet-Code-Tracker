# Last updated: 8/30/2026, 1:44:06 PM
1class Solution:
2    def numDecodings(self, s):
3        n = len(s)
4        dp = [0] * (n + 1)
5        dp[0] = 1
6
7        if s[0] != '0':
8            dp[1] = 1
9
10        for i in range(2, n + 1):
11            if s[i - 1] != '0':
12                dp[i] += dp[i - 1]
13
14            if 10 <= int(s[i - 2:i]) <= 26:
15                dp[i] += dp[i - 2]
16
17        return dp[n]
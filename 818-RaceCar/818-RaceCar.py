# Last updated: 10/1/2026, 9:15:14 AM
1class Solution:
2    def racecar(self, target):
3        dp = [0] * (target + 1)
4
5        for t in range(1, target + 1):
6            n = t.bit_length()
7
8            if (1 << n) - 1 == t:
9                dp[t] = n
10                continue
11
12            dp[t] = n + 1 + dp[(1 << n) - 1 - t]
13
14            for m in range(n - 1):
15                distance = (1 << (n - 1)) - (1 << m)
16                remaining = t - distance
17
18                dp[t] = min(
19                    dp[t],
20                    (n - 1) + 1 + m + 1 + dp[remaining]
21                )
22
23        return dp[target]
24        
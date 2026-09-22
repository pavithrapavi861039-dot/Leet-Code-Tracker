# Last updated: 9/22/2026, 9:26:20 AM
1class Solution:
2    def checkRecord(self, n):
3        MOD = 10**9 + 7
4
5        dp = [[0] * 3 for _ in range(2)]
6        dp[0][0] = 1
7
8        for _ in range(n):
9            new = [[0] * 3 for _ in range(2)]
10
11            for a in range(2):
12                for l in range(3):
13                    value = dp[a][l]
14
15                    if value == 0:
16                        continue
17
18                    # Add P
19                    new[a][0] = (new[a][0] + value) % MOD
20
21                    # Add L
22                    if l < 2:
23                        new[a][l + 1] = (new[a][l + 1] + value) % MOD
24
25                    # Add A
26                    if a < 1:
27                        new[a + 1][0] = (new[a + 1][0] + value) % MOD
28
29            dp = new
30
31        answer = 0
32
33        for a in range(2):
34            for l in range(3):
35                answer = (answer + dp[a][l]) % MOD
36
37        return answer
38        
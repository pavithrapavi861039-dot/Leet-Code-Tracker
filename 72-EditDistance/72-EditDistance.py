# Last updated: 8/30/2026, 1:39:41 PM
1class Solution:
2    def minDistance(self, word1, word2):
3        m = len(word1)
4        n = len(word2)
5        dp = [[0] * (n + 1) for _ in range(m + 1)]
6        for i in range(m + 1):
7            dp[i][0] = i
8        for j in range(n + 1):
9            dp[0][j] = j
10        for i in range(1, m + 1):
11            for j in range(1, n + 1):
12
13                if word1[i - 1] == word2[j - 1]:
14                    dp[i][j] = dp[i - 1][j - 1]
15
16                else:
17                    dp[i][j] = 1 + min(
18                        dp[i][j - 1],      
19                        dp[i - 1][j],      
20                        dp[i - 1][j - 1]   
21                    )
22
23        return dp[m][n]
24        
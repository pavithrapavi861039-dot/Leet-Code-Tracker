// Last updated: 7/17/2026, 2:54:30 PM
1class Solution {
2    public boolean isMatch(String s, String p) {
3        int m = s.length(), n = p.length();
4        boolean[][] dp = new boolean[m + 1][n + 1];
5        dp[0][0] = true;
6        for (int j = 1; j <= n; j++) {
7            if (p.charAt(j - 1) == '*') {
8                dp[0][j] = dp[0][j - 1];
9            }
10        }
11        for (int i = 1; i <= m; i++) {
12            for (int j = 1; j <= n; j++) {
13                char sc = s.charAt(i - 1);
14                char pc = p.charAt(j - 1);
15                if (pc == sc || pc == '?') {
16                    dp[i][j] = dp[i - 1][j - 1];
17                } else if (pc == '*') {
18                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
19                }
20            }
21        }
22        return dp[m][n];
23    }
24}
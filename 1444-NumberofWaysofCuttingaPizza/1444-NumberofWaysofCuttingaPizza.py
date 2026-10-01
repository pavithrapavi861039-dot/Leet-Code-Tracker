# Last updated: 10/1/2026, 9:41:50 AM
1class Solution:
2    def ways(self, pizza, k):
3        MOD = 1000000007
4        rows = len(pizza)
5        cols = len(pizza[0])
6
7        # Prefix sum of apples
8        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
9
10        for r in range(rows - 1, -1, -1):
11            for c in range(cols - 1, -1, -1):
12                prefix[r][c] = (
13                    prefix[r + 1][c]
14                    + prefix[r][c + 1]
15                    - prefix[r + 1][c + 1]
16                    + (1 if pizza[r][c] == 'A' else 0)
17                )
18
19        def apples(r1, c1, r2, c2):
20            return (
21                prefix[r1][c1]
22                - prefix[r2][c1]
23                - prefix[r1][c2]
24                + prefix[r2][c2]
25            )
26
27        # dp[r][c] = ways to cut pizza[r:][c:] into remaining pieces
28        dp = [[0] * cols for _ in range(rows)]
29
30        # One piece: valid if it contains at least one apple
31        for r in range(rows):
32            for c in range(cols):
33                if apples(r, c, rows, cols) > 0:
34                    dp[r][c] = 1
35
36        for pieces in range(2, k + 1):
37            new_dp = [[0] * cols for _ in range(rows)]
38
39            for r in range(rows):
40                for c in range(cols):
41
42                    # Horizontal cuts
43                    for nr in range(r + 1, rows):
44                        if apples(r, c, nr, cols) > 0:
45                            new_dp[r][c] += dp[nr][c]
46
47                    # Vertical cuts
48                    for nc in range(c + 1, cols):
49                        if apples(r, c, rows, nc) > 0:
50                            new_dp[r][c] += dp[r][nc]
51
52                    new_dp[r][c] %= MOD
53
54            dp = new_dp
55
56        return dp[0][0]
57        
# Last updated: 9/17/2026, 9:51:35 AM
1class Solution:
2    def canCross(self, stones):
3        n = len(stones)
4        
5        if stones[1] != 1:
6            return False
7        
8        dp = {stone: set() for stone in stones}
9        dp[0].add(0)
10        
11        for stone in stones:
12            for jump in dp[stone]:
13                for step in (jump - 1, jump, jump + 1):
14                    if step > 0 and stone + step in dp:
15                        dp[stone + step].add(step)
16        
17        return len(dp[stones[-1]]) > 0
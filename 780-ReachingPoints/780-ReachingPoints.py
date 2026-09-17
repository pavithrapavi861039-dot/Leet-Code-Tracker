# Last updated: 9/17/2026, 10:08:22 AM
1class Solution:
2    def reachingPoints(self, sx, sy, tx, ty):
3        while tx >= sx and ty >= sy:
4            if tx == sx and ty == sy:
5                return True
6
7            if tx > ty:
8                if ty == sy:
9                    return (tx - sx) % ty == 0
10                tx %= ty
11            else:
12                if tx == sx:
13                    return (ty - sy) % tx == 0
14                ty %= tx
15
16        return False
17        
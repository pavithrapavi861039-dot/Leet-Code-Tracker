# Last updated: 7/25/2026, 9:24:24 AM
1class Solution:
2    def shortestToChar(self, s, c):
3        n = len(s)
4        res = [n] * n
5        prev = -n
6        for i in range(n):
7            if s[i] == c:
8                prev = i
9            res[i] = i - prev
10        prev = 2 * n
11        for i in range(n - 1, -1, -1):
12            if s[i] == c:
13                prev = i
14            res[i] = min(res[i], prev - i)
15        return res
16        
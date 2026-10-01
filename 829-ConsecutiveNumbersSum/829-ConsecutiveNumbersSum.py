# Last updated: 10/1/2026, 9:24:59 AM
1class Solution:
2    def consecutiveNumbersSum(self, n):
3        count = 0
4        k = 1
5
6        while k * (k + 1) // 2 <= n:
7            total = k * (k - 1) // 2
8
9            if (n - total) % k == 0:
10                count += 1
11
12            k += 1
13
14        return count
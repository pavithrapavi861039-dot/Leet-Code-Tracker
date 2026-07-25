# Last updated: 7/25/2026, 9:40:40 AM
1class Solution:
2    def findKthNumber(self, m, n, k):
3        def count(x):
4            total = 0
5            for i in range(1, m + 1):
6                total += min(x // i, n)
7            return total
8        left, right = 1, m * n
9        while left < right:
10            mid = (left + right) // 2
11            if count(mid) < k:
12                left = mid + 1
13            else:
14                right = mid
15        return left
16        
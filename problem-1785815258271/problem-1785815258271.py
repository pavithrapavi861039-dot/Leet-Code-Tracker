# Last updated: 8/4/2026, 9:17:38 AM
1class Solution(object):
2    def findKthNumber(self, n, k):
3        def count_steps(n, curr, next_):
4            steps = 0
5            while curr <= n:
6                steps += min(n + 1, next_) - curr
7                curr *= 10
8                next_ *= 10
9            return steps
10        curr = 1
11        k -= 1 
12        while k > 0:
13            steps = count_steps(n, curr, curr + 1)
14            if steps <= k:
15                curr += 1
16                k -= steps
17            else:
18                curr *= 10
19                k -= 1
20        return curr
21        
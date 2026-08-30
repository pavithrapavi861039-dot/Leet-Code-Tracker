# Last updated: 8/30/2026, 1:42:41 PM
1class Solution:
2    def grayCode(self, n):
3        return [i ^ (i >> 1) for i in range(1 << n)]
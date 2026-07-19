# Last updated: 7/19/2026, 3:42:20 PM
1class Solution:
2    def strStr(self, haystack, needle):
3        n, m = len(haystack), len(needle)
4        for i in range(n - m + 1):
5            if haystack[i:i + m] == needle:
6                return i
7        return -1
8        
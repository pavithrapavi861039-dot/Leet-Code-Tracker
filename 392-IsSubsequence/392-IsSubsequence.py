# Last updated: 7/25/2026, 9:17:24 AM
1class Solution:
2    def isSubsequence(self, s, t):
3        i = j = 0
4        while i < len(s) and j < len(t):
5            if s[i] == t[j]:
6                i += 1
7            j += 1
8        return i == len(s)
9        
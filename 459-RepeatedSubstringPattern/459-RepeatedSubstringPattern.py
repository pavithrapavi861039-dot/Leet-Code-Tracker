# Last updated: 7/25/2026, 9:20:40 AM
1class Solution:
2    def repeatedSubstringPattern(self, s):
3        doubled = s + s
4        return s in doubled[1:-1]
5        
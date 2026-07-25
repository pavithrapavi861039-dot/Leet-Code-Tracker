# Last updated: 7/25/2026, 9:23:07 AM
1class Solution:
2    def reverseWords(self, s):
3        return ' '.join(word[::-1] for word in s.split())
4        
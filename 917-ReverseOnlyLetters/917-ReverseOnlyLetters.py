# Last updated: 7/25/2026, 9:25:34 AM
1class Solution:
2    def reverseOnlyLetters(self, s):
3        s = list(s)
4        left, right = 0, len(s) - 1
5        while left < right:
6            if not s[left].isalpha():
7                left += 1
8            elif not s[right].isalpha():
9                right -= 1
10            else:
11                s[left], s[right] = s[right], s[left]
12                left += 1
13                right -= 1
14        return ''.join(s)
15        
# Last updated: 7/19/2026, 3:37:15 PM
1class Solution:
2    def validPalindrome(self, s):
3        def is_palindrome(l, r):
4            while l < r:
5                if s[l] != s[r]:
6                    return False
7                l += 1
8                r -= 1
9            return True
10        left, right = 0, len(s) - 1
11        while left < right:
12            if s[left] != s[right]:
13                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
14            left += 1
15            right -= 1
16        return True
17        
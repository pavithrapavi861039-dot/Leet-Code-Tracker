# Last updated: 7/19/2026, 3:34:52 PM
1class Solution:
2    def countSubstrings(self, s):
3        def expand(left, right):
4            count = 0
5            while left >= 0 and right < len(s) and s[left] == s[right]:
6                count += 1
7                left -= 1
8                right += 1
9            return count
10        result = 0
11        for i in range(len(s)):
12            result += expand(i, i)      
13            result += expand(i, i + 1)   
14        return result
15        
# Last updated: 7/25/2026, 9:16:21 AM
1class Solution:
2    def reverseVowels(self, s):
3        vowels = set('aeiouAEIOU')
4        s = list(s)
5        left, right = 0, len(s) - 1
6        while left < right:
7            while left < right and s[left] not in vowels:
8                left += 1
9            while left < right and s[right] not in vowels:
10                right -= 1
11            s[left], s[right] = s[right], s[left]
12            left += 1
13            right -= 1
14        return ''.join(s)
15        
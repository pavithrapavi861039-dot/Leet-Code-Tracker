# Last updated: 7/25/2026, 9:06:19 AM
1class Solution:
2    def canConstruct(self, ransomNote, magazine):
3        from collections import Counter
4        count = Counter(magazine)
5        for char in ransomNote:
6            if count[char] == 0:
7                return False
8            count[char] -= 1
9        return True
10        
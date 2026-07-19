# Last updated: 7/19/2026, 3:40:03 PM
1class Solution:
2    def closeStrings(self, word1, word2):
3        if len(word1) != len(word2):
4            return False
5        from collections import Counter
6        c1 = Counter(word1)
7        c2 = Counter(word2)
8        if set(c1.keys()) != set(c2.keys()):
9            return False
10        return sorted(c1.values()) == sorted(c2.values())
11        
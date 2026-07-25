# Last updated: 7/25/2026, 9:26:35 AM
class Solution:
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False
        from collections import Counter
        c1 = Counter(word1)
        c2 = Counter(word2)
        if set(c1.keys()) != set(c2.keys()):
            return False
        return sorted(c1.values()) == sorted(c2.values())
        
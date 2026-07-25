# Last updated: 7/25/2026, 9:22:10 AM
1class Solution:
2    def detectCapitalUse(self, word):
3        return (
4            word.isupper() or
5            word.islower() or
6            word.istitle()
7        )
8        
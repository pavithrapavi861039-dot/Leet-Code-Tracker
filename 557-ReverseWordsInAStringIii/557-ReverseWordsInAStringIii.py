# Last updated: 7/31/2026, 9:34:04 AM
class Solution:
    def reverseWords(self, s):
        return ' '.join(word[::-1] for word in s.split())
        
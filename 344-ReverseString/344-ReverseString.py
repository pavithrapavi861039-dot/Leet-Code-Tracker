# Last updated: 7/16/2026, 4:07:32 PM
class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
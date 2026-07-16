# Last updated: 7/16/2026, 4:10:45 PM
class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric (left)
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric (right)
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
        
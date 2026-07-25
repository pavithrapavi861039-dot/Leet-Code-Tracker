# Last updated: 7/25/2026, 9:27:08 AM
class Solution:
    def rotateString(self, s, goal):
        return len(s) == len(goal) and goal in (s + s)
        
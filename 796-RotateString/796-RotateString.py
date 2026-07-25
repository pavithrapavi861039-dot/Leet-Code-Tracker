# Last updated: 7/25/2026, 9:13:12 AM
1class Solution:
2    def rotateString(self, s, goal):
3        return len(s) == len(goal) and goal in (s + s)
4        
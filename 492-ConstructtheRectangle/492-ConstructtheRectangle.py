# Last updated: 9/17/2026, 10:24:51 AM
1class Solution:
2    def constructRectangle(self, area):
3        w = int(area ** 0.5)
4
5        while area % w != 0:
6            w -= 1
7
8        return [area // w, w]
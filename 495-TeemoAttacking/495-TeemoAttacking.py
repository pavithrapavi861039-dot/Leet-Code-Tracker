# Last updated: 9/17/2026, 10:26:28 AM
1class Solution:
2    def findPoisonedDuration(self, timeSeries, duration):
3        total = 0
4
5        for i in range(len(timeSeries) - 1):
6            total += min(duration, timeSeries[i + 1] - timeSeries[i])
7
8        return total + duration
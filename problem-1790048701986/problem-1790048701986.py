# Last updated: 9/22/2026, 9:15:01 AM
1class Solution:
2    def poorPigs(self, buckets, minutesToDie, minutesToTest):
3        rounds = minutesToTest // minutesToDie
4        states = rounds + 1
5        pigs = 0
6
7        while states ** pigs < buckets:
8            pigs += 1
9
10        return pigs
11        
# Last updated: 9/17/2026, 10:17:35 AM
1class Solution:
2    def findComplement(self, num):
3        bits = num.bit_length()
4        mask = (1 << bits) - 1
5        return num ^ mask
# Last updated: 9/17/2026, 10:18:49 AM
1class Solution:
2    def findComplement(self, num):
3        binary = bin(num)[2:]
4        complement = ""
5        for bit in binary:
6            if bit == "0":
7                complement += "1"
8            else:
9                complement += "0"
10        return int(complement, 2)
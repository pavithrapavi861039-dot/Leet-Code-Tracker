# Last updated: 7/25/2026, 9:09:16 AM
1class Solution:
2    def addBinary(self, a, b):
3        i, j = len(a) - 1, len(b) - 1
4        carry = 0
5        result = []
6        while i >= 0 or j >= 0 or carry:
7            bit1 = int(a[i]) if i >= 0 else 0
8            bit2 = int(b[j]) if j >= 0 else 0
9            total = bit1 + bit2 + carry
10            result.append(str(total % 2)) 
11            carry = total // 2             
12            i -= 1
13            j -= 1
14        return ''.join(result[::-1])
15        
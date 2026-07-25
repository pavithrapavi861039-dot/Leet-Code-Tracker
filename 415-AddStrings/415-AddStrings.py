# Last updated: 7/25/2026, 9:07:46 AM
1class Solution:
2    def addStrings(self, num1, num2):
3        i, j = len(num1) - 1, len(num2) - 1
4        carry = 0
5        result = []
6        while i >= 0 or j >= 0 or carry:
7            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
8            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
9            total = n1 + n2 + carry
10            result.append(str(total % 10))
11            carry = total // 10
12            i -= 1
13            j -= 1
14        return ''.join(result[::-1])
15        
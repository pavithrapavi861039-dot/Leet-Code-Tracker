# Last updated: 7/19/2026, 3:33:17 PM
1class Solution:
2    def multiply(self, num1, num2):
3        if num1 == "0" or num2 == "0":
4            return "0"
5        m, n = len(num1), len(num2)
6        result = [0] * (m + n)
7        for i in range(m - 1, -1, -1):
8            for j in range(n - 1, -1, -1):
9                mul = int(num1[i]) * int(num2[j])
10                p1 = i + j
11                p2 = i + j + 1
12                total = mul + result[p2]
13                result[p2] = total % 10
14                result[p1] += total // 10
15        result_str = ''.join(map(str, result)).lstrip('0')
16        return result_str
17        
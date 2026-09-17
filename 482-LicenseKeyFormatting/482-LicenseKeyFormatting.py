# Last updated: 9/17/2026, 10:19:51 AM
1class Solution:
2    def licenseKeyFormatting(self, s, k):
3        s = s.replace("-", "").upper()
4        first = len(s) % k
5        result = []
6
7        if first:
8            result.append(s[:first])
9
10        for i in range(first, len(s), k):
11            result.append(s[i:i + k])
12
13        return "-".join(result)
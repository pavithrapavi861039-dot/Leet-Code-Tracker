# Last updated: 8/30/2026, 1:45:53 PM
1class Solution:
2    def restoreIpAddresses(self, s):
3        result = []
4
5        def backtrack(start, parts):
6            if len(parts) == 4:
7                if start == len(s):
8                    result.append(".".join(parts))
9                return
10
11            for end in range(start + 1, min(start + 4, len(s) + 1)):
12                part = s[start:end]
13
14                if len(part) > 1 and part[0] == '0':
15                    continue
16
17                if int(part) > 255:
18                    continue
19
20                parts.append(part)
21                backtrack(end, parts)
22                parts.pop()
23
24        backtrack(0, [])
25        return result
26
# Last updated: 10/1/2026, 9:22:41 AM
1class Solution:
2    def uniqueLetterString(self, s):
3        last = [-1] * 26
4        prev = [-1] * 26
5        result = 0
6
7        for i in range(len(s)):
8            x = ord(s[i]) - ord('A')
9
10            result += (i - last[x]) * (last[x] - prev[x])
11
12            prev[x] = last[x]
13            last[x] = i
14
15        for x in range(26):
16            result += (len(s) - last[x]) * (last[x] - prev[x])
17
18        return result
19        
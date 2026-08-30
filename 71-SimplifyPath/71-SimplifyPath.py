# Last updated: 8/30/2026, 1:37:57 PM
1class Solution:
2    def simplifyPath(self, path):
3        stack = []
4        parts = path.split('/')
5        for part in parts:
6            if part == "" or part == ".":
7                continue
8            elif part == "..":
9                if stack:
10                    stack.pop()
11            else:
12                stack.append(part)
13        return "/" + "/".join(stack)
14        
# Last updated: 8/30/2026, 1:36:23 PM
1class Solution:
2    def maximalRectangle(self, matrix):
3        if not matrix:
4            return 0
5        rows = len(matrix)
6        cols = len(matrix[0])
7        heights = [0] * cols
8        max_area = 0
9        for i in range(rows):
10            for j in range(cols):
11                if matrix[i][j] == '1':
12                    heights[j] += 1
13                else:
14                    heights[j] = 0
15            stack = [-1]
16            for j in range(cols):
17                while stack[-1] != -1 and heights[stack[-1]] > heights[j]:
18                    h = heights[stack.pop()]
19                    w = j - stack[-1] - 1
20                    max_area = max(max_area, h * w)
21                stack.append(j)
22            while stack[-1] != -1:
23                h = heights[stack.pop()]
24                w = cols - stack[-1] - 1
25                max_area = max(max_area, h * w)
26        return max_area
27        
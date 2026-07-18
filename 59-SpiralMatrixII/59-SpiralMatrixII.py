# Last updated: 7/18/2026, 9:13:36 PM
1class Solution:
2    def generateMatrix(self, n: int) -> List[List[int]]:
3        matrix = [[0] * n for _ in range(n)]
4        top, bottom = 0, n - 1
5        left, right = 0, n - 1
6        num = 1
7        while top <= bottom and left <= right:
8            for j in range(left, right + 1):
9                matrix[top][j] = num
10                num += 1
11            top += 1
12            for i in range(top, bottom + 1):
13                matrix[i][right] = num
14                num += 1
15            right -= 1
16            if top <= bottom:
17                for j in range(right, left - 1, -1):
18                    matrix[bottom][j] = num
19                    num += 1
20                bottom -= 1
21            if left <= right:
22                for i in range(bottom, top - 1, -1):
23                    matrix[i][left] = num
24                    num += 1
25                left += 1
26        return matrix
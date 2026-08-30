# Last updated: 8/30/2026, 1:40:41 PM
1class Solution:
2    def setZeroes(self, matrix):
3        m = len(matrix)
4        n = len(matrix[0])
5        first_row = False
6        first_col = False
7
8        for j in range(n):
9            if matrix[0][j] == 0:
10                first_row = True
11
12        for i in range(m):
13            if matrix[i][0] == 0:
14                first_col = True
15
16        for i in range(1, m):
17            for j in range(1, n):
18                if matrix[i][j] == 0:
19                    matrix[i][0] = 0
20                    matrix[0][j] = 0
21
22        for i in range(1, m):
23            for j in range(1, n):
24                if matrix[i][0] == 0 or matrix[0][j] == 0:
25                    matrix[i][j] = 0
26
27        if first_row:
28            for j in range(n):
29                matrix[0][j] = 0
30
31        if first_col:
32            for i in range(m):
33                matrix[i][0] = 0
34        
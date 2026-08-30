# Last updated: 8/30/2026, 1:48:59 PM
1class Solution:
2    def exist(self, board, word):
3        m = len(board)
4        n = len(board[0])
5
6        def dfs(r, c, i):
7            if i == len(word):
8                return True
9
10            if r < 0 or r >= m or c < 0 or c >= n:
11                return False
12
13            if board[r][c] != word[i]:
14                return False
15
16            temp = board[r][c]
17            board[r][c] = '#'
18
19            found = (
20                dfs(r + 1, c, i + 1) or
21                dfs(r - 1, c, i + 1) or
22                dfs(r, c + 1, i + 1) or
23                dfs(r, c - 1, i + 1)
24            )
25
26            board[r][c] = temp
27
28            return found
29
30        for r in range(m):
31            for c in range(n):
32                if board[r][c] == word[0]:
33                    if dfs(r, c, 0):
34                        return True
35
36        return False
37        
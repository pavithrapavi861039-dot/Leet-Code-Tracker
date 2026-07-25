# Last updated: 7/25/2026, 9:44:46 AM
1class Solution:
2    def cutOffTree(self, forest):
3        if not forest or not forest[0]:
4            return -1
5        m, n = len(forest), len(forest[0])
6        trees = [(forest[i][j], i, j)
7                 for i in range(m)
8                 for j in range(n)
9                 if forest[i][j] > 1]
10        trees.sort()
11        from collections import deque
12        def bfs(sx, sy, tx, ty):
13            if sx == tx and sy == ty:
14                return 0
15            visited = set()
16            queue = deque([(sx, sy, 0)])
17            visited.add((sx, sy))
18            while queue:
19                x, y, steps = queue.popleft()
20                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
21                    nx, ny = x + dx, y + dy
22                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and forest[nx][ny] != 0:
23                        if nx == tx and ny == ty:
24                            return steps + 1
25                        visited.add((nx, ny))
26                        queue.append((nx, ny, steps + 1))
27            
28            return -1
29        total_steps = 0
30        cx, cy = 0, 0
31        for _, tx, ty in trees:
32            dist = bfs(cx, cy, tx, ty)
33            if dist == -1:
34                return -1
35            total_steps += dist
36            cx, cy = tx, ty
37        return total_steps
38        
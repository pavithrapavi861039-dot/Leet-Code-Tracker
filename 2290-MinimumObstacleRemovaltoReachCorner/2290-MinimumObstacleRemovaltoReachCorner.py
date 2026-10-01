# Last updated: 10/1/2026, 9:54:12 AM
1from collections import deque
2
3class Solution:
4    def minimumObstacles(self, grid):
5        rows = len(grid)
6        cols = len(grid[0])
7
8        dist = [[float('inf')] * cols for _ in range(rows)]
9        dist[0][0] = 0
10
11        dq = deque([(0, 0)])
12
13        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
14
15        while dq:
16            r, c = dq.popleft()
17
18            for dr, dc in directions:
19                nr = r + dr
20                nc = c + dc
21
22                if 0 <= nr < rows and 0 <= nc < cols:
23                    cost = grid[nr][nc]
24
25                    if dist[r][c] + cost < dist[nr][nc]:
26                        dist[nr][nc] = dist[r][c] + cost
27
28                        if cost == 0:
29                            dq.appendleft((nr, nc))
30                        else:
31                            dq.append((nr, nc))
32
33        return dist[rows - 1][cols - 1]
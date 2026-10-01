# Last updated: 10/1/2026, 9:20:17 AM
1class Solution:
2    def largestIsland(self, grid):
3        n = len(grid)
4        island_id = 2
5        sizes = {}
6
7        def dfs(r, c):
8            if r < 0 or r >= n or c < 0 or c >= n:
9                return 0
10
11            if grid[r][c] != 1:
12                return 0
13
14            grid[r][c] = island_id
15
16            return (1 +
17                    dfs(r + 1, c) +
18                    dfs(r - 1, c) +
19                    dfs(r, c + 1) +
20                    dfs(r, c - 1))
21
22        for r in range(n):
23            for c in range(n):
24                if grid[r][c] == 1:
25                    sizes[island_id] = dfs(r, c)
26                    island_id += 1
27
28        answer = 0
29
30        for size in sizes.values():
31            answer = max(answer, size)
32
33        for r in range(n):
34            for c in range(n):
35                if grid[r][c] == 0:
36                    total = 1
37                    seen = set()
38
39                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
40                        nr = r + dr
41                        nc = c + dc
42
43                        if 0 <= nr < n and 0 <= nc < n:
44                            idx = grid[nr][nc]
45
46                            if idx > 1 and idx not in seen:
47                                total += sizes[idx]
48                                seen.add(idx)
49
50                    answer = max(answer, total)
51
52        return answer
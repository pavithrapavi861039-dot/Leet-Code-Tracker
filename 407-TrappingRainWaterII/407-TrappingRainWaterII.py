# Last updated: 9/17/2026, 9:53:01 AM
1import heapq
2
3class Solution:
4    def trapRainWater(self, heightMap):
5        m = len(heightMap)
6        n = len(heightMap[0])
7
8        if m < 3 or n < 3:
9            return 0
10
11        heap = []
12        visited = [[False] * n for _ in range(m)]
13
14        for i in range(m):
15            for j in [0, n - 1]:
16                heapq.heappush(heap, (heightMap[i][j], i, j))
17                visited[i][j] = True
18
19        for j in range(n):
20            for i in [0, m - 1]:
21                if not visited[i][j]:
22                    heapq.heappush(heap, (heightMap[i][j], i, j))
23                    visited[i][j] = True
24
25        water = 0
26        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
27
28        while heap:
29            height, i, j = heapq.heappop(heap)
30
31            for di, dj in directions:
32                ni = i + di
33                nj = j + dj
34
35                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
36                    visited[ni][nj] = True
37                    new_height = max(height, heightMap[ni][nj])
38                    water += max(0, height - heightMap[ni][nj])
39                    heapq.heappush(heap, (new_height, ni, nj))
40
41        return water
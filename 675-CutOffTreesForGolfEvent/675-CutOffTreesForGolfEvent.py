# Last updated: 7/25/2026, 9:56:04 AM
class Solution:
    def cutOffTree(self, forest):
        if not forest or not forest[0]:
            return -1
        m, n = len(forest), len(forest[0])
        trees = [(forest[i][j], i, j)
                 for i in range(m)
                 for j in range(n)
                 if forest[i][j] > 1]
        trees.sort()
        from collections import deque
        def bfs(sx, sy, tx, ty):
            if sx == tx and sy == ty:
                return 0
            visited = set()
            queue = deque([(sx, sy, 0)])
            visited.add((sx, sy))
            while queue:
                x, y, steps = queue.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and forest[nx][ny] != 0:
                        if nx == tx and ny == ty:
                            return steps + 1
                        visited.add((nx, ny))
                        queue.append((nx, ny, steps + 1))
            
            return -1
        total_steps = 0
        cx, cy = 0, 0
        for _, tx, ty in trees:
            dist = bfs(cx, cy, tx, ty)
            if dist == -1:
                return -1
            total_steps += dist
            cx, cy = tx, ty
        return total_steps
        
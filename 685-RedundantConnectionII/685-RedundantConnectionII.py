# Last updated: 7/25/2026, 9:53:44 AM
1class Solution:
2    def findRedundantDirectedConnection(self, edges):
3        n = len(edges)
4        parent = list(range(n + 1))
5        candidate1 = None
6        candidate2 = None
7        for u, v in edges:
8            if parent[v] != v:
9                candidate1 = [parent[v], v]
10                candidate2 = [u, v]
11                break
12            parent[v] = u
13        def find(x):
14            if uf[x] != x:
15                uf[x] = find(uf[x])
16            return uf[x]
17        def union(x, y):
18            px, py = find(x), find(y)
19            if px == py:
20                return False
21            uf[py] = px
22            return True
23        uf = list(range(n + 1))
24        for u, v in edges:
25            if candidate2 and [u, v] == candidate2:
26                continue
27            if not union(u, v):
28                if not candidate1:
29                    return [u, v]
30                return candidate1
31        return candidate2
32        
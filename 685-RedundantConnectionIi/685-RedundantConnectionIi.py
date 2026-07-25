# Last updated: 7/25/2026, 9:56:00 AM
class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))
        candidate1 = None
        candidate2 = None
        for u, v in edges:
            if parent[v] != v:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
                break
            parent[v] = u
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            uf[py] = px
            return True
        uf = list(range(n + 1))
        for u, v in edges:
            if candidate2 and [u, v] == candidate2:
                continue
            if not union(u, v):
                if not candidate1:
                    return [u, v]
                return candidate1
        return candidate2
        
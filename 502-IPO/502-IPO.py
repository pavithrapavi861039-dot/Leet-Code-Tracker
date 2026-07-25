# Last updated: 7/25/2026, 9:29:58 AM
1import heapq
2class Solution:
3    def findMaximizedCapital(self, k, w, profits, capital):
4        projects = list(zip(capital, profits))
5        projects.sort()
6        max_heap = []
7        i = 0
8        n = len(projects)
9        for _ in range(k):
10            while i < n and projects[i][0] <= w:
11                heapq.heappush(max_heap, -projects[i][1])
12                i += 1
13            if not max_heap:
14                break
15            w += -heapq.heappop(max_heap)
16        return w
17        
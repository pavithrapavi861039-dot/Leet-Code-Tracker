# Last updated: 10/1/2026, 9:12:30 AM
1class Solution:
2    def sumOfDistancesInTree(self, n, edges):
3        graph = [[] for _ in range(n)]
4
5        for a, b in edges:
6            graph[a].append(b)
7            graph[b].append(a)
8
9        count = [1] * n
10        answer = [0] * n
11
12        def dfs(node, parent):
13            for nei in graph[node]:
14                if nei == parent:
15                    continue
16
17                dfs(nei, node)
18                count[node] += count[nei]
19                answer[node] += answer[nei] + count[nei]
20
21        def dfs2(node, parent):
22            for nei in graph[node]:
23                if nei == parent:
24                    continue
25
26                answer[nei] = answer[node] - count[nei] + (n - count[nei])
27                dfs2(nei, node)
28
29        dfs(0, -1)
30        dfs2(0, -1)
31
32        return answer
33        
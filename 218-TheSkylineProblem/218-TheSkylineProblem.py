# Last updated: 9/17/2026, 9:40:24 AM
1import heapq
2
3class Solution:
4    def getSkyline(self, buildings):
5        events = []
6        for left, right, height in buildings:
7            events.append((left, -height, right))
8            events.append((right, 0, 0))
9        events.sort()
10        result = []
11        heap = [(0, float('inf'))]
12        prev_height = 0
13        for x, neg_height, right in events:
14            while heap[0][1] <= x:
15                heapq.heappop(heap)
16            if neg_height != 0:
17                heapq.heappush(heap, (neg_height, right))
18            current_height = -heap[0][0]
19            if current_height != prev_height:
20                result.append([x, current_height])
21                prev_height = current_height
22        return result
23        
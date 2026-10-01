# Last updated: 10/1/2026, 9:13:50 AM
1from collections import defaultdict, deque
2
3class Solution:
4    def numBusesToDestination(self, routes, source, target):
5        if source == target:
6            return 0
7
8        stop_to_buses = defaultdict(list)
9
10        for i in range(len(routes)):
11            for stop in routes[i]:
12                stop_to_buses[stop].append(i)
13
14        queue = deque([(source, 0)])
15        visited_stops = {source}
16        visited_buses = set()
17
18        while queue:
19            stop, buses = queue.popleft()
20
21            for bus in stop_to_buses[stop]:
22                if bus in visited_buses:
23                    continue
24
25                visited_buses.add(bus)
26
27                for next_stop in routes[bus]:
28                    if next_stop == target:
29                        return buses + 1
30
31                    if next_stop not in visited_stops:
32                        visited_stops.add(next_stop)
33                        queue.append((next_stop, buses + 1))
34
35        return -1
36        
# Last updated: 9/17/2026, 9:50:41 AM
1class Solution:
2    def isRectangleCover(self, rectangles):
3        points = set()
4        area = 0
5
6        min_x = float('inf')
7        min_y = float('inf')
8        max_x = float('-inf')
9        max_y = float('-inf')
10
11        for x1, y1, x2, y2 in rectangles:
12            area += (x2 - x1) * (y2 - y1)
13
14            min_x = min(min_x, x1)
15            min_y = min(min_y, y1)
16            max_x = max(max_x, x2)
17            max_y = max(max_y, y2)
18
19            corners = [
20                (x1, y1),
21                (x1, y2),
22                (x2, y1),
23                (x2, y2)
24            ]
25
26            for point in corners:
27                if point in points:
28                    points.remove(point)
29                else:
30                    points.add(point)
31
32        if area != (max_x - min_x) * (max_y - min_y):
33            return False
34
35        if points != {
36            (min_x, min_y),
37            (min_x, max_y),
38            (max_x, min_y),
39            (max_x, max_y)
40        }:
41            return False
42
43        return True
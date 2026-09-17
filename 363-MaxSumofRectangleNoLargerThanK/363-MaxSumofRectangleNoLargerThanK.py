# Last updated: 9/17/2026, 9:46:11 AM
1from bisect import bisect_left
2class Solution:
3    def maxSumSubmatrix(self, matrix, k):
4        rows = len(matrix)
5        cols = len(matrix[0])
6        if rows > cols:
7            matrix = list(map(list, zip(*matrix)))
8            rows, cols = cols, rows
9        answer = float("-inf")
10        for left in range(cols):
11            row_sum = [0] * rows
12            for right in range(left, cols):
13                for r in range(rows):
14                    row_sum[r] += matrix[r][right]
15                prefix = [0]
16                current_sum = 0
17                for value in row_sum:
18                    current_sum += value
19                    target = current_sum - k
20                    index = bisect_left(prefix, target)
21                    if index < len(prefix):
22                        answer = max(answer, current_sum - prefix[index])
23                    prefix.insert(bisect_left(prefix, current_sum), current_sum)
24
25        return answer
26        
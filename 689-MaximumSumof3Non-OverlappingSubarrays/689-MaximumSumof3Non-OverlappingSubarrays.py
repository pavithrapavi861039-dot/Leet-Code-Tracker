# Last updated: 9/22/2026, 9:24:08 AM
1class Solution:
2    def maxSumOfThreeSubarrays(self, nums, k):
3        n = len(nums)
4
5        prefix = [0] * (n + 1)
6
7        for i in range(n):
8            prefix[i + 1] = prefix[i] + nums[i]
9
10        sums = [0] * (n - k + 1)
11
12        for i in range(len(sums)):
13            sums[i] = prefix[i + k] - prefix[i]
14
15        left = [0] * len(sums)
16        best = 0
17
18        for i in range(len(sums)):
19            if sums[i] > sums[best]:
20                best = i
21            left[i] = best
22
23        right = [0] * len(sums)
24        best = len(sums) - 1
25
26        for i in range(len(sums) - 1, -1, -1):
27            if sums[i] >= sums[best]:
28                best = i
29            right[i] = best
30
31        max_sum = 0
32        answer = []
33
34        for j in range(k, len(sums) - k):
35            i = left[j - k]
36            l = right[j + k]
37
38            total = sums[i] + sums[j] + sums[l]
39
40            if total > max_sum:
41                max_sum = total
42                answer = [i, j, l]
43
44        return answer
45        
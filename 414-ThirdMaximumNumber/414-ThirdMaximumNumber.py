# Last updated: 7/19/2026, 3:28:45 PM
1class Solution:
2    def thirdMax(self, nums):
3        first = second = third = None
4        for num in nums:
5            if num == first or num == second or num == third:
6                continue
7            if first is None or num > first:
8                third = second
9                second = first
10                first = num
11            elif second is None or num > second:
12                third = second
13                second = num
14            elif third is None or num > third:
15                third = num
16        return third if third is not None else first
17        
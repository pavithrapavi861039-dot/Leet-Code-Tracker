# Last updated: 9/17/2026, 10:27:28 AM
1class Solution:
2    def nextGreaterElement(self, nums1, nums2):
3        stack = []
4        greater = {}
5
6        for num in nums2:
7            while stack and stack[-1] < num:
8                greater[stack.pop()] = num
9            stack.append(num)
10
11        while stack:
12            greater[stack.pop()] = -1
13
14        return [greater[num] for num in nums1]
# Last updated: 7/31/2026, 9:35:35 AM
1class Solution(object):
2    def maxNumber(self, nums1, nums2, k):
3        def maxSubsequence(nums, k):
4            stack = []
5            drop = len(nums) - k
6            for num in nums:
7                while drop and stack and stack[-1] < num:
8                    stack.pop()
9                    drop -= 1
10                stack.append(num)
11            return stack[:k]
12        def merge(seq1, seq2):
13            result = []
14            while seq1 or seq2:
15                if seq1 > seq2:
16                    result.append(seq1.pop(0))
17                else:
18                    result.append(seq2.pop(0))
19            return result
20        best = []
21        m, n = len(nums1), len(nums2)
22        for i in range(max(0, k - n), min(k, m) + 1):
23            subseq1 = maxSubsequence(nums1, i)
24            subseq2 = maxSubsequence(nums2, k - i)
25            candidate = merge(subseq1[:], subseq2[:])
26            if candidate > best:
27                best = candidate
28        return best
# Last updated: 7/31/2026, 9:37:51 AM
1class Solution(object):
2    def countRangeSum(self, nums, lower, upper):
3        prefix = [0]
4        for num in nums:
5            prefix.append(prefix[-1] + num)
6        def merge_sort(lo, hi):
7            if hi - lo <= 1:
8                return 0
9            mid = (lo + hi) // 2
10            count = merge_sort(lo, mid) + merge_sort(mid, hi)
11            j = k = mid
12            temp = []
13            r = mid
14            for left in prefix[lo:mid]:
15                while k < hi and prefix[k] - left < lower:
16                    k += 1
17                while j < hi and prefix[j] - left <= upper:
18                    j += 1
19                count += (j - k)
20            l, r = lo, mid
21            sorted_part = []
22            while l < mid and r < hi:
23                if prefix[l] < prefix[r]:
24                    sorted_part.append(prefix[l])
25                    l += 1
26                else:
27                    sorted_part.append(prefix[r])
28                    r += 1
29            sorted_part.extend(prefix[l:mid])
30            sorted_part.extend(prefix[r:hi])
31            prefix[lo:hi] = sorted_part
32            return count
33        return merge_sort(0, len(prefix))
34        
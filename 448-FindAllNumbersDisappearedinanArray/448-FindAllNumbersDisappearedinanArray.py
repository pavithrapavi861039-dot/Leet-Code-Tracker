# Last updated: 7/19/2026, 3:27:03 PM
1class Solution:
2    def findDisappearedNumbers(self, nums):
3        for num in nums:
4            index = abs(num) - 1
5            if nums[index] > 0:
6                nums[index] = -nums[index]
7        result = []
8        for i in range(len(nums)):
9            if nums[i] > 0:
10                result.append(i + 1)
11        return result
12        
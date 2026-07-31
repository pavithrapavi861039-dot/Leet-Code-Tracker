# Last updated: 7/31/2026, 9:33:41 AM
class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        def count(mid):
            cnt = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                cnt += right - left
            return cnt
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2 
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
        
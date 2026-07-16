// Last updated: 7/16/2026, 4:04:21 PM
import java.util.*;
class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        Map<Integer, Long> map = new HashMap<>();
        long prefixSum = 0;
        long maxSum = Long.MIN_VALUE;
        for (int num : nums) {
            if (map.containsKey(num - k)) {
                maxSum = Math.max(maxSum, prefixSum + num - map.get(num - k));
            }
            if (map.containsKey(num + k)) {
                maxSum = Math.max(maxSum, prefixSum + num - map.get(num + k));
            }
            map.put(num, Math.min(map.getOrDefault(num, Long.MAX_VALUE), prefixSum));

            prefixSum += num;
        }
        return maxSum == Long.MIN_VALUE ? 0 : maxSum;
    }
}
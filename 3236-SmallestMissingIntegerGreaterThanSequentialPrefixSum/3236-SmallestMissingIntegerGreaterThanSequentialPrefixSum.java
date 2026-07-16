// Last updated: 7/16/2026, 4:04:30 PM
import java.util.*;
class Solution {
    public int missingInteger(int[] nums) {
        int n = nums.length;
        int sum = nums[0];
        for (int i = 1; i < n; i++) {
            if (nums[i] == nums[i - 1] + 1) {
                sum += nums[i];
            } else {
                break;
            }
        }
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        int x = sum;
        while (set.contains(x)) {
            x++;
        }
        return x;
    }
}
// Last updated: 7/16/2026, 4:04:31 PM
import java.util.*;
class Solution {
    public int maximumSetSize(int[] nums1, int[] nums2) {
        int n = nums1.length;
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        Set<Integer> union = new HashSet<>();
        for (int num : nums1) {
            set1.add(num);
            union.add(num);
        }
        for (int num : nums2) {
            set2.add(num);
            union.add(num);
        }
        int take1 = Math.min(set1.size(), n / 2);
        int take2 = Math.min(set2.size(), n / 2);
        return Math.min(union.size(), take1 + take2);
    }
}
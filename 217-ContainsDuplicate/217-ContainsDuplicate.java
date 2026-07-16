// Last updated: 7/16/2026, 4:08:18 PM
import java.util.*;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (set.contains(num)) {
                return true;   
            }
            set.add(num);
        }
        return false;  
    }
}
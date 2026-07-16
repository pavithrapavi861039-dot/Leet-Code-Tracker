// Last updated: 7/16/2026, 4:04:43 PM
import java.util.*;
class Solution {
    public boolean checkIfExist(int[] arr) {
        Set<Integer> set = new HashSet<>();
        for (int num : arr) {
            if (set.contains(2 * num)) {
                return true;
            }
            if (num % 2 == 0 && set.contains(num / 2)) {
                return true;
            }
            set.add(num);
        }
        return false;
    }
}
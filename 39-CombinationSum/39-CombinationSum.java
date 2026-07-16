// Last updated: 7/16/2026, 4:13:47 PM
import java.util.*;
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(0, candidates, target, new ArrayList<>(), res);
        return res;
    }
    private void backtrack(int index, int[] nums, int target, List<Integer> path, List<List<Integer>> res) {
        if (target == 0) {
            res.add(new ArrayList<>(path));
            return;
        }
        if (index == nums.length || target < 0) {
            return;
        }
        path.add(nums[index]);
        backtrack(index, nums, target - nums[index], path, res);
        path.remove(path.size() - 1);
        backtrack(index + 1, nums, target, path, res);
    }
}
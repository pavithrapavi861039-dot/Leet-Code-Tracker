// Last updated: 7/17/2026, 2:58:52 PM
1class Solution {
2    public String getPermutation(int n, int k) {
3        List<Integer> nums = new ArrayList<>();
4        int[] fact = new int[n + 1];
5        fact[0] = 1;
6        for (int i = 1; i <= n; i++) {
7            fact[i] = fact[i - 1] * i;
8            nums.add(i);
9        }
10        k--; 
11        StringBuilder result = new StringBuilder();
12        for (int i = n; i >= 1; i--) {
13            int index = k / fact[i - 1];
14            result.append(nums.get(index));
15            nums.remove(index);
16
17            k %= fact[i - 1];
18        }
19        return result.toString();
20    }
21}
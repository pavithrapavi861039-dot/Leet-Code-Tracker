// Last updated: 7/17/2026, 2:53:01 PM
1class Solution {
2    public int trap(int[] height) {
3        int left = 0, right = height.length - 1;
4        int leftMax = 0, rightMax = 0;
5        int water = 0;
6        while (left < right) {
7            if (height[left] < height[right]) {
8                if (height[left] >= leftMax) {
9                    leftMax = height[left];
10                } else {
11                    water += leftMax - height[left];
12                }
13                left++;
14            } else {
15                if (height[right] >= rightMax) {
16                    rightMax = height[right];
17                } else {
18                    water += rightMax - height[right];
19                }
20                right--;
21            }
22        }
23        return water;
24    }
25}
// Last updated: 7/17/2026, 3:03:22 PM
1class Solution {
2    public int largestRectangleArea(int[] heights) {
3        Stack<Integer> stack = new Stack<>();
4        int maxArea = 0;
5        int n = heights.length;
6        for (int i = 0; i <= n; i++) {
7            int h = (i == n) ? 0 : heights[i];
8            while (!stack.isEmpty() && h < heights[stack.peek()]) {
9                int height = heights[stack.pop()];
10                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
11                maxArea = Math.max(maxArea, height * width);
12            }
13
14            stack.push(i);
15        }
16        return maxArea;
17    }
18}
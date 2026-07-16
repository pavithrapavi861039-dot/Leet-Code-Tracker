// Last updated: 7/16/2026, 4:15:57 PM
class Solution {
    public static int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int width = right - left;
            int area = Math.min(height[left], height[right]) * width;
            maxArea = Math.max(maxArea, area);

            // Move the shorter line to try increasing the area
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }

    public static void main(String[] args) {
        int[] height1 = {1,8,6,2,5,4,8,3,7};
        System.out.println(maxArea(height1)); // 49

        int[] height2 = {1,1};
        System.out.println(maxArea(height2)); // 1
    }
}

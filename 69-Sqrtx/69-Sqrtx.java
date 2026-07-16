// Last updated: 7/16/2026, 4:12:28 PM
class Solution {
    public int mySqrt(int x) {
        if (x == 0) return 0;
        int left = 1, right = x, ans = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if ((long)mid * mid == x) {
                return mid;
            } else if ((long)mid * mid < x) {
                ans = mid;       
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.mySqrt(4)); 
        System.out.println(s.mySqrt(8)); 
    }
}
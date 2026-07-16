// Last updated: 7/16/2026, 4:06:03 PM
class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        long sum = 0, sumSq = 0;
        for (int num : nums) {
            sum += num;
            sumSq += (long) num * num;
        }
        long expectedSum = (long) n * (n + 1) / 2;
        long expectedSq = (long) n * (n + 1) * (2 * n + 1) / 6;
        long diff = sum - expectedSum; 
        long diffSq = sumSq - expectedSq;
        long sumXY = diffSq / diff;
        int x = (int) ((diff + sumXY) / 2); 
        int y = (int) (x - diff);           
        return new int[]{x, y};
    }
}
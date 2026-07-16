// Last updated: 7/16/2026, 4:04:48 PM
class Solution {
    public static int subtractProductAndSum(int n) {
        int product = 1;
        int sum = 0;
        while (n > 0) {
            int d = n % 10;
            product = product * d;
            sum = sum + d;
            n = n / 10;
        }
        return product - sum;
    }
    public static void main(String[] args) {
        System.out.println(subtractProductAndSum(234));  // 15
        System.out.println(subtractProductAndSum(4421)); // 21
    }
}

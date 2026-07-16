// Last updated: 7/16/2026, 4:04:34 PM
class Solution {
    public static int passThePillow(int n, int time) {
        int person = 1;
        int direction = 1; 
        for (int i = 0; i < time; i++) {
            person += direction;
            if (person == n || person == 1) {
                direction *= -1;
            }
        }
        return person;
    }

    public static void main(String[] args) {
        System.out.println(passThePillow(4, 5)); // Output: 2
        System.out.println(passThePillow(3, 2)); // Output: 3
    }
}

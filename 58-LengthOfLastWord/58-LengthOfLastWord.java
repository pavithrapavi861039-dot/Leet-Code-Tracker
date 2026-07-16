// Last updated: 7/16/2026, 4:12:59 PM
class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();  
        int count = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == ' ') break;
            count++;
        }
        return count;
    }
}
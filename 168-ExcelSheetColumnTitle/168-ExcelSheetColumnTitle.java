// Last updated: 7/16/2026, 4:09:39 PM
class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder result = new StringBuilder();
        while (columnNumber > 0) {
            columnNumber--; 
            int remainder = columnNumber % 26;
            result.insert(0, (char)('A' + remainder));
            columnNumber /= 26;
        }
        return result.toString();
    }
}
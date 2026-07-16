// Last updated: 7/16/2026, 4:07:14 PM
class Solution {
    public int compress(char[] chars) {
        int i = 0;      
        int index = 0;  
        
        while (i < chars.length) {
            char current = chars[i];
            int count = 0;
            
            
            while (i < chars.length && chars[i] == current) {
                i++;
                count++;
            }
            
            
            chars[index++] = current;
            
            
            if (count > 1) {
                String num = Integer.toString(count);
                for (char c : num.toCharArray()) {
                    chars[index++] = c;
                }
            }
        }
        
        return index;
    }
}
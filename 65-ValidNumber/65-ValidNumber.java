// Last updated: 7/17/2026, 3:01:13 PM
1class Solution {
2    public boolean isNumber(String s) {
3        boolean seenDigit = false;
4        boolean seenDot = false;
5        boolean seenExp = false;
6        for (int i = 0; i < s.length(); i++) {
7            char c = s.charAt(i);
8            if (Character.isDigit(c)) {
9                seenDigit = true;
10            } 
11            else if (c == '+' || c == '-') {
12                if (i > 0 && s.charAt(i - 1) != 'e' && s.charAt(i - 1) != 'E') {
13                    return false;
14                }
15            } 
16            else if (c == '.') {
17                if (seenDot || seenExp) return false;
18                seenDot = true;
19            } 
20            else if (c == 'e' || c == 'E') {
21                if (seenExp || !seenDigit) return false;
22                seenExp = true;
23                seenDigit = false;
24            } 
25            else {
26                return false;
27            }
28        }
29        return seenDigit;
30    }
31}
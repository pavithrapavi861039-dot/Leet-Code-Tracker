// Last updated: 7/17/2026, 3:05:52 PM
1class Solution {
2    public int calculate(String s) {
3        int result = 0;
4        int number = 0;
5        int sign = 1;
6        Stack<Integer> stack = new Stack<>();
7        for (int i = 0; i < s.length(); i++) {
8            char c = s.charAt(i);
9            if (Character.isDigit(c)) {
10                number = number * 10 + (c - '0');
11            } 
12            else if (c == '+') {
13                result += sign * number;
14                number = 0;
15                sign = 1;
16            } 
17            else if (c == '-') {
18                result += sign * number;
19                number = 0;
20                sign = -1;
21            } 
22            else if (c == '(') {
23                stack.push(result);
24                stack.push(sign);
25
26                result = 0;
27                sign = 1;
28            } 
29            else if (c == ')') {
30                result += sign * number;
31                number = 0;
32                result *= stack.pop();
33                result += stack.pop(); 
34            }
35        }
36        result += sign * number;
37        return result;
38    }
39}
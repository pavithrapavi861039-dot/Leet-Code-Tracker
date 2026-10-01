# Last updated: 10/1/2026, 9:58:46 AM
1class Solution:
2    def kMirror(self, k, n):
3        def is_palindrome_base_k(num):
4            digits = []
5
6            while num > 0:
7                digits.append(num % k)
8                num //= k
9
10            return digits == digits[::-1]
11
12        def make_palindrome(x, odd):
13            s = str(x)
14
15            if odd:
16                return int(s + s[-2::-1])
17            else:
18                return int(s + s[::-1])
19
20        count = 0
21        total = 0
22        length = 1
23
24        while count < n:
25            half_len = (length + 1) // 2
26
27            start = 1 if half_len == 1 else 10 ** (half_len - 1)
28            end = 10 ** half_len
29
30            for x in range(start, end):
31                num = make_palindrome(x, length % 2 == 1)
32
33                if is_palindrome_base_k(num):
34                    total += num
35                    count += 1
36
37                    if count == n:
38                        return total
39
40            length += 1
41
42        return total
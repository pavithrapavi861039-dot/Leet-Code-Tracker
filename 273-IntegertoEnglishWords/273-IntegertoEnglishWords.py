# Last updated: 9/22/2026, 9:22:24 AM
1class Solution:
2    def numberToWords(self, num):
3        if num == 0:
4            return "Zero"
5
6        ones = [
7            "", "One", "Two", "Three", "Four", "Five",
8            "Six", "Seven", "Eight", "Nine", "Ten",
9            "Eleven", "Twelve", "Thirteen", "Fourteen",
10            "Fifteen", "Sixteen", "Seventeen", "Eighteen",
11            "Nineteen"
12        ]
13
14        tens = [
15            "", "", "Twenty", "Thirty", "Forty",
16            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
17        ]
18
19        def convert(n):
20            if n < 20:
21                return ones[n]
22
23            if n < 100:
24                return tens[n // 10] + ((" " + ones[n % 10]) if n % 10 else "")
25
26            return ones[n // 100] + " Hundred" + (
27                (" " + convert(n % 100)) if n % 100 else ""
28            )
29
30        result = []
31
32        if num >= 1000000000:
33            result.append(convert(num // 1000000000))
34            result.append("Billion")
35            num %= 1000000000
36
37        if num >= 1000000:
38            result.append(convert(num // 1000000))
39            result.append("Million")
40            num %= 1000000
41
42        if num >= 1000:
43            result.append(convert(num // 1000))
44            result.append("Thousand")
45            num %= 1000
46
47        if num > 0:
48            result.append(convert(num))
49
50        return " ".join(result)
51        
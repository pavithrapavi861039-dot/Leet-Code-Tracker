# Last updated: 7/25/2026, 9:05:11 AM
1class Solution:
2    def wordPattern(self, pattern, s):
3        words = s.split()
4        if len(pattern) != len(words):
5            return False
6        char_to_word = {}
7        word_to_char = {}
8        for c, w in zip(pattern, words):
9            if c in char_to_word:
10                if char_to_word[c] != w:
11                    return False
12            else:
13                char_to_word[c] = w
14            if w in word_to_char:
15                if word_to_char[w] != c:
16                    return False
17            else:
18                word_to_char[w] = c
19        return True
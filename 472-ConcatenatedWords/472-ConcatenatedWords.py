# Last updated: 7/25/2026, 10:02:47 AM
1class Solution:
2    def findAllConcatenatedWordsInADict(self, words):
3        word_set = set(words)
4        memo = {}
5        def canForm(word):
6            if word in memo:
7                return memo[word]
8            for i in range(1, len(word)):
9                prefix = word[:i]
10                suffix = word[i:]
11                if prefix in word_set:
12                    if suffix in word_set or canForm(suffix):
13                        memo[word] = True
14                        return True
15            memo[word] = False
16            return False
17        res = []
18        for word in words:
19            word_set.remove(word)
20            if canForm(word):
21                res.append(word)
22            word_set.add(word)
23        return res
24        
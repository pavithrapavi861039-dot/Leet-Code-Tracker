# Last updated: 9/17/2026, 9:48:43 AM
1import random
2
3class RandomizedCollection:
4
5    def __init__(self):
6        self.nums = []
7        self.indices = {}
8
9    def insert(self, val):
10        if val not in self.indices:
11            self.indices[val] = set()
12            result = True
13        else:
14            result = False
15
16        self.nums.append(val)
17        self.indices[val].add(len(self.nums) - 1)
18
19        return result
20
21    def remove(self, val):
22        if val not in self.indices or not self.indices[val]:
23            return False
24
25        remove_index = self.indices[val].pop()
26        last_val = self.nums[-1]
27        last_index = len(self.nums) - 1
28
29        self.nums[remove_index] = last_val
30
31        if remove_index != last_index:
32            self.indices[last_val].remove(last_index)
33            self.indices[last_val].add(remove_index)
34        self.nums.pop()
35        if not self.indices[val]:
36            del self.indices[val]
37        return True
38    def getRandom(self):
39        return random.choice(self.nums)
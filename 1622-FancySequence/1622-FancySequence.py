# Last updated: 10/1/2026, 9:44:06 AM
1class Fancy:
2
3    def __init__(self):
4        self.mod = 1000000007
5        self.arr = []
6        self.mul = 1
7        self.add = 0
8
9    def append(self, val):
10        val = (val - self.add) * pow(self.mul, self.mod - 2, self.mod)
11        self.arr.append(val % self.mod)
12
13    def addAll(self, inc):
14        self.add = (self.add + inc) % self.mod
15
16    def multAll(self, m):
17        self.mul = (self.mul * m) % self.mod
18        self.add = (self.add * m) % self.mod
19
20    def getIndex(self, idx):
21        if idx >= len(self.arr):
22            return -1
23
24        return (self.arr[idx] * self.mul + self.add) % self.mod
# Last updated: 10/1/2026, 9:10:57 AM
1class Solution:
2    def minCameraCover(self, root):
3        self.cameras = 0
4
5        def dfs(node):
6            if node is None:
7                return 1
8
9            left = dfs(node.left)
10            right = dfs(node.right)
11
12            if left == 0 or right == 0:
13                self.cameras += 1
14                return 2
15
16            if left == 2 or right == 2:
17                return 1
18
19            return 0
20
21        if dfs(root) == 0:
22            self.cameras += 1
23
24        return self.cameras
# Last updated: 8/30/2026, 1:46:37 PM
1class Solution:
2    def generateTrees(self, n):
3        def build(start, end):
4            if start > end:
5                return [None]
6
7            trees = []
8
9            for root in range(start, end + 1):
10                left_trees = build(start, root - 1)
11                right_trees = build(root + 1, end)
12
13                for left in left_trees:
14                    for right in right_trees:
15                        node = TreeNode(root)
16                        node.left = left
17                        node.right = right
18                        trees.append(node)
19
20            return trees
21
22        return build(1, n)
23        
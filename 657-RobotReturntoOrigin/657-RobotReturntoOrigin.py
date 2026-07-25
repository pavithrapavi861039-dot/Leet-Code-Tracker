# Last updated: 7/25/2026, 9:14:33 AM
1class Solution:
2    def judgeCircle(self, moves):
3        x = y = 0
4        for move in moves:
5            if move == 'U':
6                y += 1
7            elif move == 'D':
8                y -= 1
9            elif move == 'R':
10                x += 1
11            elif move == 'L':
12                x -= 1
13        return x == 0 and y == 0
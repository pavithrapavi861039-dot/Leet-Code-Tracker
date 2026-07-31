# Last updated: 7/31/2026, 9:33:47 AM
class Solution:
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
        return x == 0 and y == 0
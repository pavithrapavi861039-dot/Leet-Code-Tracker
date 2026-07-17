// Last updated: 7/17/2026, 2:51:43 PM
1class Solution {
2    public void solveSudoku(char[][] board) {
3        solve(board);
4    }
5    private boolean solve(char[][] board) {
6        for (int i = 0; i < 9; i++) {
7            for (int j = 0; j < 9; j++) {
8                if (board[i][j] == '.') {
9                    for (char c = '1'; c <= '9'; c++) {
10                        if (isValid(board, i, j, c)) {
11                            board[i][j] = c;
12                            if (solve(board)) return true;
13                            board[i][j] = '.';
14                        }
15                    }
16
17                    return false;
18                }
19            }
20        }
21        return true; 
22    }
23    private boolean isValid(char[][] board, int row, int col, char c) {
24        for (int i = 0; i < 9; i++) {
25            if (board[row][i] == c) return false;
26            if (board[i][col] == c) return false;
27            int boxRow = 3 * (row / 3) + i / 3;
28            int boxCol = 3 * (col / 3) + i % 3;
29            if (board[boxRow][boxCol] == c) return false;
30        }
31        return true;
32    }
33}
// Last updated: 7/17/2026, 2:57:19 PM
1class Solution {
2    int count = 0;
3    public int totalNQueens(int n) {
4        boolean[] col = new boolean[n];
5        boolean[] diag1 = new boolean[2 * n]; // r + c
6        boolean[] diag2 = new boolean[2 * n]; // r - c + n
7        backtrack(0, n, col, diag1, diag2);
8        return count;
9    }
10    private void backtrack(int row, int n, boolean[] col, boolean[] diag1, boolean[] diag2) {
11        if (row == n) {
12            count++;
13            return;
14        }
15        for (int c = 0; c < n; c++) {
16            if (col[c] || diag1[row + c] || diag2[row - c + n]) continue;
17            col[c] = diag1[row + c] = diag2[row - c + n] = true;
18            backtrack(row + 1, n, col, diag1, diag2);
19            col[c] = diag1[row + c] = diag2[row - c + n] = false;
20        }
21    }
22}
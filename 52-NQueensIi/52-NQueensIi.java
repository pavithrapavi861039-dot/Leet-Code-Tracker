// Last updated: 7/17/2026, 3:04:53 PM
class Solution {
    int count = 0;
    public int totalNQueens(int n) {
        boolean[] col = new boolean[n];
        boolean[] diag1 = new boolean[2 * n]; // r + c
        boolean[] diag2 = new boolean[2 * n]; // r - c + n
        backtrack(0, n, col, diag1, diag2);
        return count;
    }
    private void backtrack(int row, int n, boolean[] col, boolean[] diag1, boolean[] diag2) {
        if (row == n) {
            count++;
            return;
        }
        for (int c = 0; c < n; c++) {
            if (col[c] || diag1[row + c] || diag2[row - c + n]) continue;
            col[c] = diag1[row + c] = diag2[row - c + n] = true;
            backtrack(row + 1, n, col, diag1, diag2);
            col[c] = diag1[row + c] = diag2[row - c + n] = false;
        }
    }
}
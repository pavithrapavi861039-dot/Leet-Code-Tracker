// Last updated: 7/16/2026, 4:04:18 PM
class Solution {
    public int[][] modifiedMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[] colMax = new int[n];
        for (int j = 0; j < n; j++) {
            int max = 0;
            for (int i = 0; i < m; i++) {
                max = Math.max(max, matrix[i][j]);
            }
            colMax[j] = max;
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == -1) {
                    matrix[i][j] = colMax[j];
                }
            }
        }
        return matrix;
    }
}
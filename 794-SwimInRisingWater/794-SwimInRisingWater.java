// Last updated: 7/16/2026, 4:05:45 PM
import java.util.*;
class Solution {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> a[0] - b[0]
        );
        boolean[][] visited = new boolean[n][n];
        pq.offer(new int[]{grid[0][0], 0, 0});
        visited[0][0] = true;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int time = cur[0], r = cur[1], c = cur[2];
            if (r == n - 1 && c == n - 1) {
                return time;
            }
            for (int[] d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];
                if (nr >= 0 && nc >= 0 && nr < n && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    pq.offer(new int[]{
                        Math.max(time, grid[nr][nc]),
                        nr,
                        nc
                    });
                }
            }
        }
        return -1;
    }
}
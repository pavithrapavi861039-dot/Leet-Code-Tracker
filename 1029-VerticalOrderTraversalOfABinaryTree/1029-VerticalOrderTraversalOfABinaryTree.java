// Last updated: 7/16/2026, 4:05:31 PM
import java.util.*;
class Solution {
    class Pair {
        TreeNode node;
        int row, col;
        Pair(TreeNode n, int r, int c) {
            node = n;
            row = r;
            col = c;
        }
    }
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        TreeMap<Integer, TreeMap<Integer, PriorityQueue<Integer>>> map = new TreeMap<>();
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(root, 0, 0));
        while (!q.isEmpty()) {
            Pair p = q.poll();
            map.putIfAbsent(p.col, new TreeMap<>());
            map.get(p.col).putIfAbsent(p.row, new PriorityQueue<>());
            map.get(p.col).get(p.row).add(p.node.val);
            if (p.node.left != null)
                q.add(new Pair(p.node.left, p.row + 1, p.col - 1));
            if (p.node.right != null)
                q.add(new Pair(p.node.right, p.row + 1, p.col + 1));
        }
        List<List<Integer>> result = new ArrayList<>();
        for (TreeMap<Integer, PriorityQueue<Integer>> rows : map.values()) {
            List<Integer> colList = new ArrayList<>();
            for (PriorityQueue<Integer> pq : rows.values()) {
                while (!pq.isEmpty()) {
                    colList.add(pq.poll());
                }
            }
            result.add(colList);
        }
        return result;
    }
}
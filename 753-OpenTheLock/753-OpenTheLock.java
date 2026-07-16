// Last updated: 7/16/2026, 4:05:55 PM
import java.util.*;
class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> dead = new HashSet<>(Arrays.asList(deadends));
        Set<String> visited = new HashSet<>();
        Queue<String> q = new LinkedList<>();
        if (dead.contains("0000")) return -1;
        q.add("0000");
        visited.add("0000");
        int steps = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                String curr = q.poll();
                if (curr.equals(target)) return steps;
                for (String next : getNext(curr)) {
                    if (!dead.contains(next) && !visited.contains(next)) {
                        q.add(next);
                        visited.add(next);
                    }
                }
            }
            steps++;
        }
        return -1;
    }
    private List<String> getNext(String s) {
        List<String> res = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            char[] ch = s.toCharArray();
            ch[i] = (char)((ch[i] - '0' + 1) % 10 + '0');
            res.add(new String(ch));
            ch = s.toCharArray();
            ch[i] = (char)((ch[i] - '0' + 9) % 10 + '0');
            res.add(new String(ch));
        }
        return res;
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        String[] dead = {"0201","0101","0102","1212","2002"};
        String target = "0202";
        System.out.println(s.openLock(dead, target)); 
    }
}
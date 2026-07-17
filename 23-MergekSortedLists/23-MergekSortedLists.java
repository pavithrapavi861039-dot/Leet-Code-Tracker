// Last updated: 7/17/2026, 2:43:24 PM
1import java.util.*;
2class Solution {
3    public ListNode mergeKLists(ListNode[] lists) {
4        if (lists == null || lists.length == 0) return null;
5        PriorityQueue<ListNode> pq = new PriorityQueue<>(
6            (a, b) -> a.val - b.val
7        );
8        for (ListNode node : lists) {
9            if (node != null) {
10                pq.offer(node);
11            }
12        }
13        ListNode dummy = new ListNode(0);
14        ListNode tail = dummy;
15        while (!pq.isEmpty()) {
16            ListNode minNode = pq.poll();
17            tail.next = minNode;
18            tail = tail.next;
19            if (minNode.next != null) {
20                pq.offer(minNode.next);
21            }
22        }
23        return dummy.next;
24    }
25}
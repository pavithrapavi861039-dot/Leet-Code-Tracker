// Last updated: 7/17/2026, 2:47:45 PM
1class Solution {
2    public ListNode reverseKGroup(ListNode head, int k) {
3        if (head == null || k == 1) return head;
4        ListNode dummy = new ListNode(0);
5        dummy.next = head;
6        ListNode prevGroupEnd = dummy;
7        while (true) {
8            ListNode kth = getKthNode(prevGroupEnd, k);
9            if (kth == null) break;
10            ListNode nextGroupStart = kth.next;
11            ListNode prev = nextGroupStart;
12            ListNode curr = prevGroupEnd.next;
13            while (curr != nextGroupStart) {
14                ListNode temp = curr.next;
15                curr.next = prev;
16                prev = curr;
17                curr = temp;
18            }
19            ListNode temp = prevGroupEnd.next;
20            prevGroupEnd.next = kth;
21            prevGroupEnd = temp;
22        }
23        return dummy.next;
24    }
25    private ListNode getKthNode(ListNode curr, int k) {
26        while (curr != null && k > 0) {
27            curr = curr.next;
28            k--;
29        }
30        return curr;
31    }
32}
// Last updated: 7/16/2026, 4:12:03 PM
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode curr = head;

        while (curr != null && curr.next != null) {
            if (curr.val == curr.next.val) {
                curr.next = curr.next.next; // remove duplicate
            } else {
                curr = curr.next; // move forward
            }
        }

        return head;
    }
}
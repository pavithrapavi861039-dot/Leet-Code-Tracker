// Last updated: 7/16/2026, 4:08:19 PM
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;

        while (head != null) {
            ListNode next = head.next; 
            head.next = prev;        
            prev = head;               
            head = next;               
        }

        return prev;
    }
}

# Last updated: 8/30/2026, 1:44:52 PM
1class Solution:
2    def reverseBetween(self, head, left, right):
3        dummy = ListNode(0)
4        dummy.next = head
5        prev = dummy
6
7        for _ in range(left - 1):
8            prev = prev.next
9
10        curr = prev.next
11
12        for _ in range(right - left):
13            temp = curr.next
14            curr.next = temp.next
15            temp.next = prev.next
16            prev.next = temp
17
18        return dummy.next
19        
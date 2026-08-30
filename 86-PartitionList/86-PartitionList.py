# Last updated: 8/30/2026, 1:41:59 PM
1class Solution:
2    def partition(self, head, x):
3        less = ListNode(0)
4        greater = ListNode(0)
5
6        p1 = less
7        p2 = greater
8
9        while head:
10            if head.val < x:
11                p1.next = head
12                p1 = p1.next
13            else:
14                p2.next = head
15                p2 = p2.next
16            head = head.next
17
18        p2.next = None
19        p1.next = greater.next
20
21        return less.next
22        
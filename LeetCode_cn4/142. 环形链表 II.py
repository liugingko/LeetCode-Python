# Definition for singly-linked list.
from numba import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        while fast:
            slow = slow.next
            if not fast.next:
                return None
            fast = fast.next.next
            if fast == slow:
                pre = head
                while pre != slow:
                    slow = slow.next
                    pre = pre.next
                return pre

        return None

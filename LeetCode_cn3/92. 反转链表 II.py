# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        pre_head = ListNode(0, head)
        pre = pre_head

        for _ in range(left -1):
            pre = pre.next

        cur = pre.next

        for _ in range(right - left):
            tmp = cur.next
            cur.next = cur.next.next

            tmp.next = pre.next
            pre.next = tmp

        return pre_head.next








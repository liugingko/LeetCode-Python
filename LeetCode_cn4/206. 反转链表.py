# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return head

        pre = None
        cur = head
        next = head.next

        while next:

            cur.next = pre
            pre = cur
            cur = next

            next = next.next







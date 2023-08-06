# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k ==0 or not head or not head.next:
            return head

        cur = head
        n = 0
        while cur.next:
            cur = cur.next
            n += 1

        add = n - k % n

        if add == n:  # 倍数的时候
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        res = cur.next
        cur.next = None
        return res





if __name__ == '__main__':

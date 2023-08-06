# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):

        res = ListNode(0, head)
        fist = head
        second = res

        for _ in range(n):
            fist = fist.next

        while fist:

            fist = fist.next
            second = second.next

        second.next = second.next.next

        return res.next




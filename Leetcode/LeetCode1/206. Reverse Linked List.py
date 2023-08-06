# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def mergeTwoLists(self, head):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre_head = ListNode(None)

        while head:
            pre_head.next = head
            head.next = pre_head.next
            head = head.next
        return pre_head.next

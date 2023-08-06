# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l3, l1 = l1, l1.next
        else:
            l3, l2 = l2, l2.next

        cur = l3
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return l3

class Solution:
    def mergeTwoLists(self, a, b):
        if not a:return b
        if not b:return a

        if a.val < b.val:
            c, a = a, a.next
        else:
            c, b = b, b.next
        cur = c
        while a and b:

            if a.val < b.val:
                cur.next, a = a, a.next
            else:
                cur.next, b = b, b.next

            cur = cur.next

        cur.next = a if a else b

        return c

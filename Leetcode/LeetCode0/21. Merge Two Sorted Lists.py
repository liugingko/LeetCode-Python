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
        p1 = ListNode(None)
        p1.next = l1
        p2 = ListNode(None)
        p2.next = l2
        r = rp = ListNode(None)
        while(p1.next!=None or p2.next!=None):
            if p1.next!=None and p2.next!=None:
                if p1.next.val < p2.next.val:
                    r.val = p1.next.val
                    r.next = ListNode(None)
                    r = r.next
                    p1 = p1.next
                else:
                    r.val = p2.next.val
                    r.next = ListNode(None)
                    r = r.next
                    p2 = p2.next
            elif p1.next!=None and p2.next==None:
                r.val = p1.next.val
                r.next = ListNode(None)
                r = r.next
                p1 = p1.next
            elif p1.next==None and p2.next!=None:
                r.val = p2.next.val
                r.next = ListNode(None)
                r = r.next
                p2 = p2.next
        return rp

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
            if not a or b and a.val > b.val:
                a, b = b, a
            if a:
                a.next = self.mergeTwoLists(a.next, b)
            return a
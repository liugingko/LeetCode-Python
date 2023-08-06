# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def mergeTwoLists(self, list1, list2):

        if not list1: return list2
        if not list2: return list1
        if list1.val < list2.val: l3, list1 = list1, list1.next
        else:l3, list2 = list2, list2.next
        cur = l3
        while list1 and list2:
            if list1.val < list2.val:  cur.next, list1 = list1, list1.next
            else:  cur.next, list2 = list2, list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return l3

    def mergeKLists1(self, lists):

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        k = len(lists)
        res = lists[0]
        for i in range(1, k):

            res = self.mergeTwoLists(res, lists[i])

        return res

    def merge(self, lists, l, r):
        if l == r: return lists[r]

        if l > r: return None
        mid = (l + r ) >> 1

        return self.mergeTwoLists(self.merge(lists, l, mid), self.merge(lists, mid, r))
    def mergeKLists(self, lists):

        return self.merge(lists, 0, len(lists)-1)

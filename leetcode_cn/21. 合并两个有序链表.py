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
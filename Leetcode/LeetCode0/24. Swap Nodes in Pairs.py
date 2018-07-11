# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        if not head: return None
        root = ListNode(0)
        root.next = head

        slow = head  # 较慢的指针，在后面
        fast = head.next  # 较快的指针，在前面
        pre = root  # 在设置一个辅助指针

        while fast:
            slow.next = fast.next
            fast.next = slow
            pre.next = fast
            pre = slow
            if not slow.next: break
            slow = slow.next
            fast = slow.next
        return root.next
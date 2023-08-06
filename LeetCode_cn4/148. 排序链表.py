class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head

        while fast.next and fast.next.next:  # 用快慢指针分成两部分
            slow = slow.next
            fast = fast.next.next

        mid = slow.next  # 找到左右部分, 把左部分最后置空
        slow.next = None

        left = self.sortList(head)   # 递归下去
        right = self.sortList(mid)

        return self.merge(left, right)  # 合并

    def merge(self, left, right):
        dummy = ListNode(0)
        p = dummy
        l = left
        r = right

        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
                p = p.next
            else:
                p.next = r
                r = r.next
                p = p.next
        if l:
            p.next = l
        if r:
            p.next = r
        return dummy.next
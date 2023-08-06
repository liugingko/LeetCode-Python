# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        notehead = ListNode(0)
        curr = notehead
        while (l1 != None or l2 != None):
            n = l1.val if l1 != None else 0
            m = l2.val if l2 != None else 0
            sum = carry + n + m
            carry = int(sum / 10)
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next

        if carry > 0:
            curr.next = ListNode(carry)

        arr = []

        while (notehead.next != None):
            arr.append(notehead.next.val)

        return notehead.next


if __name__ == '__main__':
    l1 = ListNode(9)
    print(l1.val)
    l2 = ListNode(8)
    test = Solution()
    out = test.addTwoNumbers(l1, l2)
    print(out.val)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        l1_len = 0
        l2_len = 0
        curr1 = l1
        curr2 = l2

        while curr1 != None:
            curr1 = curr1.next
            l1_len += 1
        while curr2 != None:
            curr2 = curr2.next
            l2_len += 1

        def addZeros(head, count):
            curr = head
            while curr.next != None:
                curr = curr.next

            for _ in range(count):
                curr.next = ListNode(0)
                curr = curr.next
            return head

        if l1_len < l2_len:
            l1 = addZeros(l1, l2_len - l1_len)
        elif l2_len < l1_len:
            l2 = addZeros(l2, l1_len - l2_len)

        dummy = ListNode(0)
        curr = dummy
        carry = 0
        curr1 = l1
        curr2 = l2

        while curr1 != None:
            total = curr1.val + curr2.val + carry
            carry = total // 10
            digit = total % 10
            curr.next = ListNode(digit)
            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = l1
        carry = 0
        while l1 and l2:
            carry, l1.val = divmod(l1.val + l2.val + carry, 10)
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
            elif l2.next:
                l1.next = ListNode(0)
                l1 = l1.next
                l2 = l2.next
            elif l1.next:
                l2.next = ListNode(0)
                l1 = l1.next
                l2 = l2.next
            elif carry > 0:
                l1.next = ListNode(carry)
                break
            else:
                break

        return l3

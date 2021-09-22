# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(9999)
        dummyhead.next = head

        fast = head
        slow = dummyhead

        while fast != None:
            if fast.val == slow.val:
                slow.next = fast.next
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next

        return dummyhead.next

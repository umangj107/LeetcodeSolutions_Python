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
        prev = None

        while fast != None:
            if fast.val == slow.val:
                while fast != None and fast.val == slow.val:
                    slow.next = fast.next
                    fast = fast.next
                prev.next = fast
                if fast == None:
                    break
                else:
                    slow = slow.next
                    fast = fast.next

            else:
                fast = fast.next
                prev = slow
                slow = slow.next

        return dummyhead.next

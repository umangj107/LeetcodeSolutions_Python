# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        def get_len(h):
            count = 0
            temp = h
            while h.next:
                count += 1
                h = h.next
            h.next = temp
            return count+1

        n = get_len(head)
        k = k % n

        length = n - k
        dummyNode = ListNode(0)
        dummyNode.next = head
        curr_idx = 1
        curr_node = head

        while curr_idx != length:
            curr_idx += 1
            curr_node = curr_node.next

        temp = curr_node.next
        curr_node.next = None
        dummyNode.next = temp

        return dummyNode.next

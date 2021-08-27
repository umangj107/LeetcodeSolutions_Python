# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev_head = None
        prev_tail = None

        node = head
        length = 0
        while node != None:
            length += 1
            node = node.next

        node = head
        for _ in range(length // k):
            curr_head = None
            curr_tail = None
            for i in range(k):
                temp = node
                node = node.next
                temp.next = curr_head
                curr_head = temp
                if curr_tail == None:
                    curr_tail = temp

            if prev_head == None:
                prev_head = curr_head
                prev_tail = curr_tail
            else:
                prev_tail.next = curr_head
                prev_tail = curr_tail

        if node != None:
            prev_tail.next = node

        return prev_head

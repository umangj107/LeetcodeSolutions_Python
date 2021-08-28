# Approach-1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        else:
            while head != None:
                if head.val == -999999:
                    return True
                else:
                    head.val = -999999
                    head = head.next

            return False


# Approach-2


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        else:
            ref_set = set()
            while head != None:
                if head in ref_set:
                    return True
                else:
                    ref_set.add(head)
                    head = head.next

            return False


# Approach-3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False

        fast = head.next
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

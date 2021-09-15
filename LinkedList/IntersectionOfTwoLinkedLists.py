# Approach-1
# Slow-Approach


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ref_set = set()
        while headA != None:
            ref_set.add(headA)
            headA = headA.next
        while headB != None:
            if headB in ref_set:
                return headB
            headB = headB.next

        return None


# Approach-2
# Efficient Approach


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        listA = headA
        listB = headB

        while listA != listB:
            listA = listA.next if listA != None else headB
            listB = listB.next if listB != None else headA

        return listA

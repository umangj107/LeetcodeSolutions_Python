# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        end = head.next
        
        currSum = 0
        
        while end != None:
            if end.val != 0:
                currSum += end.val
            else:
                start = start.next
                start.val = currSum
                currSum = 0
            
            end = end.next 
           
        start.next = None
        return head.next      
        
#Working solution below:
#         
#         newHead = ListNode();
#         newTail = newHead;
        
#         ptr = head.next
        
#         currSum = 0
        
#         while ptr != None:
#             if ptr.val == 0:
#                 node = ListNode(currSum)
#                 newTail.next = node
#                 newTail = node
#                 currSum = 0
#             else:
#                 currSum += ptr.val
            
#             ptr = ptr.next
        
#         return newHead.next
        
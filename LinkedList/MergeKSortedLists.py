# Approach-1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = ListNode()
        curr = result
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        frequencyDict = {}
        for i in lists:
            while i != None:
                if i.val in frequencyDict.keys():
                    frequencyDict[i.val] += 1
                else:
                    frequencyDict[i.val] = 1
                i = i.next

        for i in sorted(frequencyDict.keys()):
            for j in range(frequencyDict[i]):
                curr.next = ListNode(i)
                curr = curr.next

        return result.next


# Approach-2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            if not list1:
                return list2
            elif not list2:
                return list1
            else:
                h1 = list1
                h2 = list2
                dummyH = ListNode()
                dummyT = dummyH
                while h1 and h2:
                    if h1.val < h2.val:
                        dummyT.next = h1
                        h1 = h1.next
                    else:
                        dummyT.next = h2
                        h2 = h2.next
                    if not dummyH.next:
                        dummyH.next = dummyT

                    dummyT = dummyT.next

                if h1:
                    dummyT.next = h1
                if h2:
                    dummyT.next = h2

            return dummyH.next

        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        curr = 0
        while len(lists) > 1:
            temp = []
            while len(lists) >= 2:
                mh = mergeTwoLists(lists[curr], lists[curr+1])
                lists.pop(0)
                lists.pop(0)
                temp.append(mh)
            if len(lists) == 1:
                temp.append(lists[0])
            lists = temp

        return lists[0]

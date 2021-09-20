# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return root

        LOT = []
        queue = [root]

        while queue:
            tempres = []
            n = len(queue)
            i = 0
            while i < n:
                x = queue.pop(0)
                i += 1
                tempres.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            LOT.append(tempres)

        for i in range(1, len(LOT), 2):
            LOT[i] = LOT[i][::-1]

        return LOT

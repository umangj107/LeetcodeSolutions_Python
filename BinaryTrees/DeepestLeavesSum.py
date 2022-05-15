# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return root.val
        else:
            queue = [root]

            while queue:
                tempQueue = []
                for x in queue:
                    if x.left:
                        tempQueue.append(x.left)
                    if x.right:
                        tempQueue.append(x.right)
                if not tempQueue:
                    return sum([x.val for x in queue])
                queue = tempQueue

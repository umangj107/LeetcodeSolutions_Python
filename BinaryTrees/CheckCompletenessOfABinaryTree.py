# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = [root]
        prevNode = root

        while queue:
            currNode = queue.pop(0)
            if currNode:
                if not prevNode:
                    return False
                queue.append(currNode.left)
                queue.append(currNode.right)
            prevNode = currNode

        return True

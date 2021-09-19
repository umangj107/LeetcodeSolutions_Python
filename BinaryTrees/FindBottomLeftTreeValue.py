# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return None
        elif root.left == None and root.right == None:
            return root.val
        queue = [root]
        while queue:
            x = queue.pop(0)
            resultNode = x
            if x.right:
                queue.append(x.right)
            if x.left:
                queue.append(x.left)

        return resultNode.val

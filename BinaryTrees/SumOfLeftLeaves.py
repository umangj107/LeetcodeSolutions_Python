# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0

        def findLeafSum(root, direc):
            if root.left == None and root.right == None and direc == -1:
                self.sum += root.val
            else:
                if root.left:
                    findLeafSum(root.left, -1)
                if root.right:
                    findLeafSum(root.right, 1)

        findLeafSum(root, 0)
        return self.sum

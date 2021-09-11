# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def func_2(self, root, low, high):
        if root == None:
            return True
        elif root.val > low and root.val < high:
            return self.func_2(root.left, low, root.val) and self.func_2(root.right, root.val, high)
        else:
            return False

    def isValidBST(self, root: TreeNode) -> bool:
        if root.left == None and root.right == None:
            return True
        return self.func_2(root, -math.inf, math.inf)

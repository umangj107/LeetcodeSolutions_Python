# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(root):
            if root == None:
                return ""
            elif root.left == None and root.right == None:
                return str(root.val) + ""
            elif root.right == None:
                return str(root.val) + "(" + str(preorder(root.left)) + ")"
            else:
                return str(root.val) + "(" + str(preorder(root.left)) + ")(" + str(preorder(root.right)) + ")"

        return preorder(root)

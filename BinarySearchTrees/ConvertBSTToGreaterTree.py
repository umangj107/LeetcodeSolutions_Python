# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def convert(root, val):
            if not root:
                return val
            root.val += convert(root.right, val)
            val = root.val
            val = convert(root.left, val)
            return val

        convert(root, 0)
        return root

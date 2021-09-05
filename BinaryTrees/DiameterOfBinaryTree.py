# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def diameter(root):
            if root == None:
                return 0
            else:
                left = diameter(root.left)
                right = diameter(root.right)

                temp = max(left, right) + 1
                ans = max(temp, left + right + 1)
                self.res = max(ans, self.res)

            return temp

        diameter(root)
        return self.res - 1

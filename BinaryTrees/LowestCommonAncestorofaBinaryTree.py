# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def recurse(currNode):
            if not currNode:
                return False

            left = recurse(currNode.left)
            right = recurse(currNode.right)

            mid = currNode == p or currNode == q
            if mid + left + right >= 2:
                self.ans = currNode

            return mid or left or right

        recurse(root)
        return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if not root.left and not root.right:
            return root
        self.inorderarr = []

        def getInorder(root):
            if root == None:
                return
            getInorder(root.left)
            self.inorderarr.append(root.val)
            getInorder(root.right)

        def reconstructTree(l, r):
            if l <= r:
                mid = (l + r) // 2
                root = TreeNode(self.inorderarr[mid])
                root.left = reconstructTree(l, mid-1)
                root.right = reconstructTree(mid+1, r)
                return root
            return None

        getInorder(root)
        return reconstructTree(0, len(self.inorderarr)-1)

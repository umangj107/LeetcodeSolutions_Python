"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode
    @return: a list of integer
    """

    def boundaryOfBinaryTree(self, root):
        self.result = []

        def printLeaves(root):
            if root:
                if root.left:
                    printLeaves(root.left)
                if root.left is None and root.right is None:
                    self.result.append(root.val)
                if root.right:
                    printLeaves(root.right)

        def printLeftBoundary(root):
            if root:
                if root.left:
                    self.result.append(root.val)
                    printLeftBoundary(root.left)
                elif root.right:
                    self.result.append(root.val)
                    printLeftBoundary(root.right)

        def printRightBoundary(root):
            if root:
                if root.right:
                    printRightBoundary(root.right)
                    self.result.append(root.val)
                elif root.left:
                    printRightBoundary(root.left)
                    self.result.append(root.val)

        if not root:
            return []
        self.result.append(root.val)
        printLeftBoundary(root.left)
        printLeaves(root)
        printRightBoundary(root.right)
        return self.result

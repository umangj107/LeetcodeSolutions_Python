# Approach-1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.preorderTraversal = []

        def preorder(root):
            if root:
                self.preorderTraversal.append(root.val)
                if root.left:
                    preorder(root.left)
                if root.right:
                    preorder(root.right)

        if root == None:
            return
        preorder(root)
        root.left = None
        root.right = None
        head = root
        for i in range(1, len(self.preorderTraversal)):
            head.right = TreeNode(self.preorderTraversal[i])
            head = head.right


# Approach-2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node.left = None
            node.right = stack[-1] if stack else None

# Approach-1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []

        def inorder(root):
            if root:
                if root.left:
                    inorder(root.left)
                self.result.append(root.val)
                if root.right:
                    inorder(root.right)

        inorder(root)
        return self.result[k-1]


# Approach-2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # In order traversal would give nondecreasing array
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root:
                if k == 1:
                    return root.val
                k -= 1
                root = root.right
        return -1

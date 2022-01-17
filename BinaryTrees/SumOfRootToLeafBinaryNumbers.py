# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.binaries = []

        def dfs(root, pattern):
            if not root:
                return

            pattern += str(root.val)
            if root.left == None and root.right == None:
                self.binaries.append(pattern)
                return
            else:
                dfs(root.left, pattern)
                dfs(root.right, pattern)

        dfs(root, '')
        result = 0
        print(self.binaries)
        for binary in self.binaries:
            result += int(binary, 2)
        return result

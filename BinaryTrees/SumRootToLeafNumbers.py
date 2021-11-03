# Approach-1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.routes = []

    def findRoutes(self, route, root):
        if root == None:
            return 0

        elif root.left == None and root.right == None:
            route = int(str(route) + str(root.val))
            self.routes.append(route)
            return

        else:
            route = int(str(route) + str(root.val))
            self.findRoutes(route, root.left)
            self.findRoutes(route, root.right)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return root.val
        else:
            self.findRoutes(0, root)
            return sum(self.routes)


# Approach-2


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, path_sum):
            if not root:
                return 0
            if (root.left is None) and (root.right is None):
                return path_sum*10 + root.val
            return dfs(root.left, path_sum*10 + root.val) + \
                dfs(root.right, path_sum*10 + root.val)
        return dfs(root, 0)

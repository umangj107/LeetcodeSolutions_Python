#Approach-1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
          
          

#Approach-2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.left == None:
            return 1+self.maxDepth(root.right)
        elif root.right==None:
            return 1+self.maxDepth(root.left)
        else:
            return 1 + max(self.maxDepth(root.right),self.maxDepth(root.left))

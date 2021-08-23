#Approach-1
#Recursive Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, result):
        if root != None:
            if root.left:
                self.inorder(root.left, result)
            result.append(root.val)
            if root.right:
                self.inorder(root.right, result)
        return
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorder(root, result)
        return result
      
      
      
#Approach-2
#Iterative Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        elif not root.left and not root.right:
            return [root.val]
        else:
            result=[]
            stack = []
            while stack or root:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    root= stack.pop(-1)
                    result.append(root.val)
                    root = root.right
                    
            return result

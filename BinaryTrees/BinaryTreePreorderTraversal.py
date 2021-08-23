#Approach-1
#Recursive Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, result):
        if root:
            result.append(root.val)
            if root.left:
                self.preorder(root.left, result)
            if root.right:
                self.preorder(root.right, result)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preorder(root, result)
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        elif not root.left and not root.right:
            return [root.val]
        else:
            result = []
            stack = [root]
            while stack:
                node = stack.pop(-1)
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                    
            return result
                

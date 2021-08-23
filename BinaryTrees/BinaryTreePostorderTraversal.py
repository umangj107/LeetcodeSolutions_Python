#Approach-1
#Recursive Approach


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, root, result):
        if root:
            if root.left:
                self.postorder(root.left, result)
            if root.right:
                self.postorder(root.right, result)
            result.append(root.val)
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postorder(root, result)
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        else:
            stack = [root, root.right, root.left]
            result = []
            while stack:
                node = stack[-1]
                if node.right:
                    stack.append(node.right)
                elif node.left:
                    stack.append(node.left)
                else:
                    node = stack.pop(-1)
                    result.append(node.val)
                    
            return result

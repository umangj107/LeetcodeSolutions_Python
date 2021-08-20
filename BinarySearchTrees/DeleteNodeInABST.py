# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMax(self, node):
        if node.right != None:
            return self.findMax(node.right)
        else:
            return node.val
    
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:  
        if root == None:
            return None
        
        else:
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            elif root.val > key:
                root.left = self.deleteNode(root.left, key)
            else:
                if not root.left and not root.right:
                    return None
                elif not root.left and root.right:
                    return root.right
                elif not root.right and root.left:
                    return root.left
                else:
                    lmax = self.findMax(root.left)
                    root.val = lmax
                    root.left = self.deleteNode(root.left,lmax)
                    
            return root

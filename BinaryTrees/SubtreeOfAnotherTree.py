# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None or root1.val != root2.val:
            return False
        return self.compare(root1.left, root2.left) and self.compare(root1.right, root2.right) 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return subRoot == None
        
        queue = [root]
        while queue:
            temp = []
            while queue:
                x = queue.pop(0)
                if x.left != None:
                    temp.append(x.left)
                if x.right != None:
                    temp.append(x.right)
                if x.val == subRoot.val and self.compare(x, subRoot):
                    return True
            queue = temp

        return False
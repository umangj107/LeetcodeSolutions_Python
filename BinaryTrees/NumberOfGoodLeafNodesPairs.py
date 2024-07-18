# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    
    def helper(self, d, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [1]
        else:
            l = self.helper(d, root.left)
            r = self.helper(d, root.right)
            
            for i in l:
                for j in r:
                    if i+j <= d:
                        self.result += 1
            
            retArr = []
            for i in l:
                if i+1 < d:
                    retArr.append(i+1)
            for j in r:
                if j+1 < d:
                    retArr.append(j+1)
            
            return retArr
    
    
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root:
            return 1
        self.helper(distance, root)
        return self.result
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        elif root.right == None and root.left == None:
            return [[root.val]]
        else:
            result = []
            queue = [root]
            while queue:
                sub_queue = []
                sub_result = []
                for i in queue:
                    sub_result.append(i.val)
                    if i.left:
                        sub_queue.append(i.left)
                    if i.right:
                        sub_queue.append(i.right)
                queue= sub_queue
                result.append(sub_result)
                
            return result[::-1]

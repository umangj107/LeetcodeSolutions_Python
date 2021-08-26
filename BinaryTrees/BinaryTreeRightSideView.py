#Approach-1

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def level_order_traversal(self,root):
        queue = [root]
        result = []
        while queue:
            result.append(queue[-1].val)
            temp_queue = []
            for i in queue:
                if i.left:
                    temp_queue.append(i.left)
                if i.right:
                    temp_queue.append(i.right)
            queue = temp_queue
        return result

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [root.val]
        else:
            return self.level_order_traversal(root)



#Approach-2
#Efficient-Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levels = {}
        def helper(node, level):
            if not node:
                return
            self.levels[level] = node.val
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
                
        helper(root, 0) 
        return self.levels.values()
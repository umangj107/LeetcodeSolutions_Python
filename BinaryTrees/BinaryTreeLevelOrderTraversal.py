#Approach-1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
      if root == None:
            return []
        elif root.left == None and root.right == None:
            return [[root.val]]
        else:
            result = []
            queue = [root]
            temp = []
            temp_res = []
            while queue:
                while queue:
                    x = queue.pop(0)
                    temp_res.append(x.val)
                    if x.left:
                        temp.append(x.left)
                    if x.right:
                        temp.append(x.right)
                queue=temp
                temp=[]
                result.append(temp_res)
                temp_res = []
                
            return result
          

#Approach-2
#Efficient

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [[root.val]]
        else:
            result = []
            queue = [root]
            while queue:
                temp = []
                res = []
                for i in queue:
                    res.append(i.val)
                    if i.left:
                        temp.append(i.left)
                    if i.right:
                        temp.append(i.right)
                queue=temp
                result.append(res)
            return result


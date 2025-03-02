# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        refDict = defaultdict(list)

        def search(node, level):
            refDict[level].append(node.val)

            if node.left:
                search(node.left, level+1)
            if node.right:
                search(node.right, level+1)

        search(root, 0)
        answer = []
        
        for levelNodes in refDict.values():
            answer.append(sum(levelNodes)/len(levelNodes))
        
        return answer
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def solve(root, d):
            vertical_dist = {}
            queue = [(root, d)]
            while len(queue) > 0:
                temp_queue = []
                tempDict = {}
                while queue:
                    root, d = queue.pop(0)
                    if d in tempDict:
                        tempDict[d].append(root.val)
                    else:
                        tempDict[d] = [root.val]
                    if root.left:
                        temp_queue.append((root.left, d-1))
                    if root.right:
                        temp_queue.append((root.right, d+1))
                queue = temp_queue
                for key in sorted(tempDict.keys()):
                    x = tempDict[key]
                    if len(x) > 1:
                        x.sort()
                    if key in vertical_dist:
                        vertical_dist[key] += x
                    else:
                        vertical_dist[key] = x

            result = []
            for i in sorted(vertical_dist.keys()):
                result.append(vertical_dist[i])

            return result

        return solve(root, 0)

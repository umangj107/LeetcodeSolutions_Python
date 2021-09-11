# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}

        def dfs(root, parent):
            parents[root] = parent
            if root.right:
                dfs(root.right, root)
            if root.left:
                dfs(root.left, root)

        dfs(root, None)

        queue = [(target, 0)]
        visited = {target}

        while queue:
            node, dist = queue.pop(0)
            if dist == k:
                return [node.val] + [node.val for node, dist in queue]

            for i in (node.left, node.right, parents[node]):
                if i and i not in visited:
                    queue.append((i, dist+1))
                    visited.add(i)

        return []

# Approach-1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            nodes.append(node)
            inOrder(node.right)

        inOrder(root)

        for i in range(len(nodes)-1):
            nodes[i].right = nodes[i+1]
            nodes[i].left = None
        nodes[-1].right = None
        nodes[-1].left = None

        return nodes[0]


# Approach-2


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                self.curr.right = node
                node.left = None
                self.curr = node
                inorder(node.right)

        ans = self.curr = TreeNode()
        inorder(root)
        return ans.right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        InorderA = []
        InorderB = []
        self.InorderM = []

        def Inorder(root):
            if root != None:
                Inorder(root.left)
                self.InorderM.append(root.val)
                Inorder(root.right)

        Inorder(root1)
        InorderA = self.InorderM
        self.InorderM = []
        Inorder(root2)
        InorderB = self.InorderM
        self.InorderM = []

        n = len(InorderA)
        m = len(InorderB)
        index = 0

        while InorderA and InorderB:
            if InorderA[0] < InorderB[0]:
                x = InorderA.pop(0)
            else:
                x = InorderB.pop(0)
            self.InorderM.append(x)

        while InorderA:
            x = InorderA.pop(0)
            self.InorderM.append(x)

        while InorderB:
            x = InorderB.pop(0)
            self.InorderM.append(x)

        return self.InorderM

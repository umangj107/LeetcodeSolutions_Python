"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        elif root.left == None and root.right == None:
            return root
        else:
            queue = [root, None]
            while len(queue) > 0:
                while queue:
                    x = queue.pop(0)
                    if x != None:
                        x.next = queue[0]
                        if x.left:
                            queue.append(x.left)
                        if x.right:
                            queue.append(x.right)

                    else:
                        if queue:
                            queue.append(None)
                        break

            return root

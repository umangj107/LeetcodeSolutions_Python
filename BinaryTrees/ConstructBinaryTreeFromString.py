"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param s: a string
    @return: a root of this tree
    """

    def str2tree(self, s):
        # write your code here
        if not s:
            return None
        if '(' not in s:
            root = TreeNode(int(s))
            return root
        else:
            idx = s.index('(')
            root = TreeNode(int(s[:idx]))
            stk, idx = ['('], idx + 1
            start = idx
            while stk:
                if s[idx] == '(':
                    stk.append('(')
                elif s[idx] == ')':
                    stk.pop()
                idx += 1
            root.left = self.str2tree(s[start:idx-1])
            root.right = self.str2tree(s[idx+1:-1])
            return root

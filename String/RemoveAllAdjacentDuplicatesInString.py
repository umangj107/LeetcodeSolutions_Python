class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1] != c:
                stack.append(c)
            else:
                stack.pop(-1)
        res = ''
        while stack:
            res += stack[-1]
            stack.pop(-1)
        return res[::-1]

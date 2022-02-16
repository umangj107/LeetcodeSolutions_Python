# Approach-1

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return False

        open = ['(', '{', '[']
        close = [')', '}', ']']
        stack = []
        for b in s:
            if b in open:
                stack.append(b)
            else:
                if not stack:
                    return False
                elif stack[-1] != open[close.index(b)]:
                    return False
                else:
                    stack.pop(-1)

        if not stack:
            return True
        else:
            return False


# Approach-2

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in dic.values():
                stack.append(c)
            elif c in dic.keys():
                if len(stack) == 0 or stack.pop() != dic[c]:
                    return False
        return stack == []

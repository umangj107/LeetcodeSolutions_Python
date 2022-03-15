# Approach-1
# Using stack

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stck = []
        result = [""]*len(s)
        for i, char in enumerate(s):
            if char not in ('(', ')'):
                result[i] = char
            elif char == '(':
                stck.append(i)
            else:
                if stck:
                    result[i] = char
                    result[stck.pop()] = '('
        return ''.join(result)


# Approach-2
# Without Using Stack


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        open = 0
        s = list(s)

        for i, c in enumerate(s):
            if c == '(':
                open += 1
            elif c == ')':
                if not open:
                    s[i] = ""
                else:
                    open -= 1

        for i in range(len(s)-1, -1, -1):
            if not open:
                break
            if s[i] == '(':
                s[i] = ""
                open -= 1

        return "".join(s)

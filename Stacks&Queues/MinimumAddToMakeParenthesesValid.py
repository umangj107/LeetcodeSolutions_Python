# Approach-1

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if stack and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    stack.append(i)

        return len(stack)


# Approach-2

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        counter = 0
        total = 0
        for i in range(len(s)):
            if s[i] == ')':
                counter -= 1
                if counter < 0:
                    total += 1
                    counter = 0
            elif s[i] == '(':
                counter += 1
        return total + counter

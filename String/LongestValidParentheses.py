# Approach-1
# Using Extra Space

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        stack = [-1]

        for i in range(len(s)):
            if not stack or s[i] == '(':
                stack.append(i)
            else:
                x = stack.pop(-1)
                if not stack:
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i-stack[-1])

        return maxLen


# Approach-2
# Without Extra Space

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right, maxLen = 0, 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxLen = max(maxLen, 2*right)
            elif right >= left:
                left, right = 0, 0

        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxLen = max(maxLen, 2*right)
            elif left >= right:
                left, right = 0, 0

        return maxLen
